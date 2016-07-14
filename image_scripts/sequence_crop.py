# -*- coding: utf-8 -*-
import os, sys, time, datetime, subprocess
sys.path.append("//Art-1405260002/d/assets/scripts/image_scripts/ui")

import multiprocessing
import Queue
import threading

import scipy.ndimage
import numpy as np

from PySide import QtCore, QtGui
import sequenceCropUi as sequenceCropUi
reload(sequenceCropUi)

class Button(QtGui.QPushButton):
    fileDropped = QtCore.Signal(unicode)
    def __init__(self, parent):
        super(Button, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Button, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(Button, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.fileDropped.emit(url.toLocalFile())
            event.acceptProposedAction()
        else:
            super(Button,self).dropEvent(event)

class LineEdit(QtGui.QLineEdit):
    fileDropped = QtCore.Signal(unicode)
    def __init__(self, parent):
        super(LineEdit, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(LineEdit, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(LineEdit, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.fileDropped.emit(url.toLocalFile())
            event.acceptProposedAction()
        else:
            super(LineEdit,self).dropEvent(event)

class MySignal(QtCore.QObject):
    dimensions = QtCore.Signal(list)
    count = QtCore.Signal(int)

class workerSignal(QtCore.QObject):
    status = QtCore.Signal(unicode)

class ListenerThread(QtCore.QThread):
    global outputQueue
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.listening = True
        self.count = 0
        self.maxLength = 1
        self.signal = MySignal()

    def run(self):
        self.outputs = []
        while self.listening == True:
            x = outputQueue.get()
            if type(x) == unicode:
                self.count = self.count + 1
                #perc = ((float(self.count) / float(self.maxLength)) * 100)
                #print str(perc) + "%"
                self.signal.count.emit(self.count)
                if self.count == self.maxLength:
                    self.count = 0
            if type(x) == list:
                self.outputs.append(x)
                self.count = self.count + 1
                #perc = ((float(self.count) / float(self.maxLength)) * 100)
                #print str(perc) + "%"
                self.signal.count.emit(self.count)
                if self.count == self.maxLength:
                    x_min, x_max, y_min, y_max = self.outputs[0]
                    for output in self.outputs:
                        a = output[0]
                        b = output[1]
                        c = output[2]
                        d = output[3]
                        if a < x_min:
                            x_min = a
                        if b > x_max:
                            x_max = b
                        if c < y_min:
                            y_min = c
                        if d > y_max:
                            y_max = d
                    x_size = x_max - x_min
                    y_size = y_max - y_min
                    dimensions = [x_size, y_size, x_min, y_min]

                    self.signal.dimensions.emit(dimensions)
                    self.count = 0


class WorkerThread(QtCore.QThread):
    global outputQueue
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.tgaConvert = False
        self.input_path = ""
        self.dimensions = []
        self.signal = workerSignal()

    def buildQueue(self):
        self.images = [f for f in os.listdir(self.input_path) if os.path.isfile(self.input_path + "/" + f)]

        q = multiprocessing.Queue()
        for image in self.images:
            q.put(image)
        q.put("STOP")
        return q

    #def multiprocessWorker(self, target, imagesQueue, input_path, outputQueue, cpuCount):
    def multiprocessWorker(self, *args):
        if len(args) == 5:
            target, imagesQueue, input_path, outputQueue, cpuCount = args
            worker_args = [imagesQueue, input_path, outputQueue]
        else:
            target, imagesQueue, input_path, outputQueue, cpuCount, x_size, y_size, x_min, y_min = args
            worker_args = [imagesQueue, input_path, outputQueue, x_size, y_size, x_min, y_min]
        jobs = []
        for x in range(cpuCount):
            try:
                self.worker = multiprocessing.Process(target=target, args=worker_args)
                self.worker.daemon = True
                jobs.append(self.worker)
                self.worker.start()
            except EOFError:
                break
            except:
                pass
        for job in jobs:
            job.join()

    def run(self):
        imagesQueue = self.buildQueue()

        if self.tgaConvert == True:
            self.signal.status.emit("Converting TGA")
            self.multiprocessWorker(worker_tga, imagesQueue, self.input_path, outputQueue, 8)
            self.input_path = self.input_path + "/tmp" # point input path to temp converted dir
            imagesQueue = self.buildQueue()

        self.signal.status.emit(u"計算圖串範圍大小中...")
        self.multiprocessWorker(worker_findMinMax, imagesQueue, self.input_path, outputQueue, 12)

        x_size, y_size, x_min, y_min = self.dimensions
        if self.tgaConvert == True:
            self.input_path = self.input_path.replace("/tmp","")
        imagesQueue = self.buildQueue()
        self.signal.status.emit(u"裁切圖串中...")
        self.multiprocessWorker(worker_crop, imagesQueue, self.input_path, outputQueue, 8, x_size, y_size, x_min, y_min)
        self.signal.status.emit("All Done!")

class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = sequenceCropUi.Ui_SequenceCrop()
        self.ui.setupUi(self)
        sshFile = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.ui.input_path = LineEdit(self)
        self.ui.input_path.setMinimumSize(QtCore.QSize(400, 80))
        self.ui.input_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.input_path.setText("")
        self.ui.input_path.setPlaceholderText(u"可以拖拉或用右邊按鈕選資料夾，資料夾內只能一串序列圖!")
        self.ui.input_path.setObjectName("input_path")
        self.ui.horizontalLayout_4.addWidget(self.ui.input_path)
        self.ui.input_path.fileDropped.connect(self.droppedPath)


        self.ui.input_folder_button = Button(self)
        self.ui.input_folder_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-open-o_d7801a_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.input_folder_button.setIcon(icon)
        self.ui.input_folder_button.setIconSize(QtCore.QSize(12, 12))
        self.ui.input_folder_button.setFlat(False)
        self.ui.input_folder_button.setObjectName("input_folder_button")
        self.ui.horizontalLayout_4.addWidget(self.ui.input_folder_button)
        self.ui.input_folder_button.fileDropped.connect(self.droppedPath)

        self.ui.output_path.hide()
        self.ui.output_label.hide()

        self.ui.input_folder_button.clicked.connect(self.selectFolder)

        self.ui.progress_bar.hide()
        self.ui.status_line.hide()

        self.ui.convert_button.clicked.connect(self.work)
        self.ui.convert_button.clicked.connect(self.listen)
        self.ui.input_path.textChanged.connect(self.checkPath)
        self.ui.input_path.textChanged.connect(self.setOutput)

        self.worker = WorkerThread()
        self.listener = ListenerThread()

        self.listener.signal.count.connect(self.progressBarCount)
        self.listener.signal.dimensions.connect(self.dimensions)
        self.worker.signal.status.connect(self.updateStatus)

        #self.ui.input_path.setText("d:/sequence/cba7")
    def droppedPath(self, url):
        self.ui.input_path.setText(url)


    def selectFolder(self):
        startingDir = 'C:/Program Files'
        dialog = QtGui.QFileDialog()
        input_path = dialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        input_path = input_path.replace("\\","/")
        self.ui.input_path.setText(input_path)
        self.checkPath()

    def updateStatus(self, data):
        self.ui.status_line.setText(data)
        if data == "All Done!":
            time.sleep(2)
            self.enableUI()
            subprocess.check_call(['explorer', self.ui.output_path.text().replace("/", "\\")])
        if data == u"裁切圖串中...":
            self.listener.count = 0

    def disableUI(self):
        self.ui.progress_bar.show()
        self.ui.status_line.show()
        self.ui.convert_button.setDisabled(True)
        self.ui.input_path.setDisabled(True)
        self.ui.input_folder_button.setDisabled(True)

    def enableUI(self):
        self.ui.progress_bar.hide()
        #self.ui.status_line.hide()
        self.ui.convert_button.setEnabled(True)
        self.ui.input_path.setEnabled(True)
        self.ui.input_folder_button.setEnabled(True)

    def checkPath(self):
        ok_ext = ['tif', 'tga', 'png', 'jpg']

        self.input_path = self.ui.input_path.text()
        ext_count = []
        name_count = []
        try:
            images = [f for f in os.listdir(self.input_path) if os.path.isfile(self.input_path + "/" + f)]
            maxLength = len(images)

            self.ui.progress_bar.setMaximum(maxLength)
            self.listener.maxLength = maxLength
            for image in images:
                fileExt = image.split(".")[-1]
                fileName = image.replace(("." + fileExt),"")
                if fileExt not in ok_ext:
                    self.ui.status_line.setText(u"不是圖檔")
                    break
                if fileExt not in ext_count:
                    ext_count.append(fileExt)
                if fileName not in name_count:
                    name_count.append(fileName)
        except:
            self.ui.status_line.setText(u"沒有圖串")

        if len(ext_count) == 1:
            ext = ext_count[0]
            if ext_count[0] == "tga":
                self.ui.status_line.setText(u"找到 TGA 圖串")
                #self.worker.tgaConvert = True
            elif ext_count[0] == "tif":
                self.ui.status_line.setText(u"找到 TIF 圖串")
        elif len(ext_count) > 1 and len(name_count) > 1:
            self.ui.status_line.setText(u"資料夾內只能有一個圖串")

    def setOutput(self):
        input_path = self.ui.input_path.text()
        output_path = input_path + "/cropped"
        self.ui.output_path.setText(output_path)

    def listen(self):
        if not self.listener.isRunning():
            self.listener.start()

    def work(self):
        if not self.worker.isRunning():
            self.worker.exiting=False
            self.worker.input_path = self.ui.input_path.text()
            self.disableUI()
            self.listener.count = 0
            self.worker.start()

    def progressBarCount(self,data):
        self.ui.progress_bar.setValue(data)

    def dimensions(self,data):
        self.worker.dimensions = data

def worker_tga(q, input_path, outputQueue):
    while True:
        try:
            image = q.get(block=True, timeout=0.1)
        except Queue.Empty:
            break
        if image == "STOP":
            break

        out_dir = input_path + "/tmp"
        image_path = input_path + "/" + image

        fileExt = image.split(".")[-1]
        fileName = image.replace(("." + fileExt),"")

        flag = "-compress zip"
        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        output_path = out_dir + "/" + fileName + ".tif"

        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, output_path)
        subprocess.call(imageMagickCMD)

        outputQueue.put(image)
    q.close()

def worker_findMinMax(q, input_path, outputQueue):
    def findWhite(im):
        count = 0
        for count, column in enumerate(im):
            if np.sum(column)/3/255 > 0:
                break
        return count

    while True:
        try:
            image = q.get(block=True, timeout=0.1)
        except Queue.Empty:
            break
        if image == "STOP":
            break

        image = input_path + "/" + image
        im = scipy.ndimage.imread(image)
        height, width, channel = im.shape
        y_min = findWhite(im)
        im_reverse = im[::-1]

        y_max = findWhite(im_reverse)
        y_max = height - y_max

        im = np.swapaxes(im,0,1)
        x_min = findWhite(im)

        im_reverse = im[::-1]
        x_max = findWhite(im_reverse)
        x_max = width - x_max

        outputQueue.put([x_min, x_max, y_min, y_max])

def worker_crop(q, input_path, outputQueue, x_size, y_size, x_min, y_min):
    while True:
        try:
            image = q.get(block=True, timeout=0.1)
        except Queue.Empty: # Queue here refers to the  module, not a class
            break
        if image == "STOP":
            break

        out_dir = input_path + "/cropped"
        image_path = input_path + "/" + image

        fileExt = image.split(".")[-1]
        fileName = image.replace(("." + fileExt),"")

        flag = "-alpha on -compress zip -crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)

        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        out_path = out_dir + "/" + fileName + ".png"

        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, out_path)
        subprocess.call(imageMagickCMD)

        outputQueue.put(u"xx" + image)

if __name__=='__main__':
    outputQueue = multiprocessing.Queue()
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())