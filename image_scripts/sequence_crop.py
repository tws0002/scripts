# -*- coding: utf-8 -*-
'''
import subprocess
import fileinput
input = "//Art-1405260002/d/assets/scripts/image_scripts/ui/sequence_crop.ui"
output = "//Art-1405260002/d/assets/scripts/image_scripts/ui/sequenceCropUi.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))
with open(output, 'r') as data:
    filedata = data.read()
header = "# -*- coding: utf-8 -*-\n"
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"
filedata = filedata.replace(':/Art-1405260002', '//Art-1405260002')
filedata = filedata.replace('import icons_rc', '')
filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)

pyinstaller --onedir --windowed --noconsole --hidden-import=scipy.linalg --hidden-import=linalg.cython_blas --hidden-import=scipy.linalg.cython_lapack --hidden-import=scipy.integrate --icon=\\Art-1405260002\d\assets\scripts\image_scripts\icons\SequenceCrop.ico sequence_crop.py
'''
import os, sys, time, subprocess
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
                    if x_size % 2 > 0:
                        x_size = x_size + 1
                    if y_size % 2 > 0:
                        y_size = y_size + 1
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
        self.images = [f for f in os.listdir(self.input_path) if os.path.isfile(self.input_path + "/" + f) and 'Thumbs.db' not in f]

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
        cpus = multiprocessing.cpu_count()
        imagesQueue = self.buildQueue()

        # if self.tgaConvert == True:
        #     self.signal.status.emit("Converting TGA")
        #     self.multiprocessWorker(worker_tga, imagesQueue, self.input_path, outputQueue, cpus)
        #     self.input_path = self.input_path + "/tmp" # point input path to temp converted dir
        #     imagesQueue = self.buildQueue()

        self.signal.status.emit(u"計算圖串範圍大小中...")
        self.multiprocessWorker(worker_findMinMax, imagesQueue, self.input_path, outputQueue, int(cpus*1.5))

        x_size, y_size, x_min, y_min = self.dimensions
        if self.tgaConvert == True:
            self.input_path = self.input_path.replace("/tmp","")
        imagesQueue = self.buildQueue()
        self.signal.status.emit(u"裁切圖串中...")
        self.multiprocessWorker(worker_crop, imagesQueue, self.input_path, outputQueue, cpus, x_size, y_size, x_min, y_min)
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
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.input_folder_button.setIcon(icon)
        self.ui.input_folder_button.setIconSize(QtCore.QSize(24, 24))
        self.ui.input_folder_button.setFlat(False)
        self.ui.input_folder_button.setObjectName("input_folder_button")
        self.ui.horizontalLayout_4.addWidget(self.ui.input_folder_button)
        self.ui.input_folder_button.fileDropped.connect(self.droppedPath)


        self.ui.output_path = LineEdit(self)
        self.ui.output_path.setMinimumSize(QtCore.QSize(400, 80))
        self.ui.output_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.output_path.setText("")
        self.ui.output_path.setPlaceholderText(u"可以拖拉或用右邊按鈕選資料夾，資料夾內只能一串序列圖!")
        self.ui.output_path.setObjectName("output_path")
        self.ui.horizontalLayout_5.addWidget(self.ui.output_path)

        self.ui.output_folder_button = Button(self)
        self.ui.output_folder_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-open-o_d7801a_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.output_folder_button.setIcon(icon)
        self.ui.output_folder_button.setIconSize(QtCore.QSize(24, 24))
        self.ui.output_folder_button.setFlat(False)
        self.ui.output_folder_button.setObjectName("output_folder_button")
        self.ui.horizontalLayout_5.addWidget(self.ui.output_folder_button)

        self.ui.status_line.setText(u"請選資料夾")
        self.ui.output_path.hide()
        self.ui.output_label.hide()
        self.ui.output_folder_button.hide()

        self.ui.input_folder_button.clicked.connect(self.selectFolder)
        self.ui.output_folder_button.clicked.connect(self.openCropped)

        self.ui.progress_bar.hide()

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
    def openCropped(self):
        FNULL = open(os.devnull, 'w')
        sys.stdout = FNULL
        subprocess.STARTF_USESHOWWINDOW = 1
        explorerCMD = "explorer %s"  % self.ui.output_path.text().replace("/", "\\")
        subprocess.call(explorerCMD.encode(sys.getfilesystemencoding()), stdout=FNULL, stderr=subprocess.STDOUT)
        self.ui.output_folder_button.hide()
        self.ui.status_line.setText(u"請選資料夾")
        self.ui.output_label.hide()
        self.ui.output_path.hide()

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
            self.finishUI()
            #subprocess.check_call(['explorer', self.ui.output_path.text().replace("/", "\\")])
        if data == u"裁切圖串中...":
            self.listener.count = 0

    def disableUI(self):
        self.ui.progress_bar.show()
        self.ui.status_line.show()
        self.ui.convert_button.setDisabled(True)
        self.ui.input_path.setDisabled(True)
        self.ui.input_folder_button.setDisabled(True)
        self.ui.output_folder_button.hide()
        self.ui.output_label.hide()
        self.ui.output_path.hide()

    def finishUI(self):
        self.ui.progress_bar.hide()
        self.ui.output_folder_button.show()
        self.ui.convert_button.setEnabled(True)
        self.ui.input_path.setEnabled(True)
        self.ui.input_folder_button.setEnabled(True)
        self.ui.output_label.show()
        self.ui.output_path.show()

    def checkPath(self):
        ok_ext = ['tif', 'tga', 'png', 'jpg']

        self.input_path = self.ui.input_path.text()
        ext_count = []
        name_count = []
        try:
            images = [f for f in os.listdir(self.input_path) if os.path.isfile(self.input_path + "/" + f) and 'Thumbs.db' not in f]
            maxLength = len(images)
        except:
            self.ui.status_line.setText(u"")

        if len(images) > 0:
            self.ui.progress_bar.setMaximum(maxLength)
            self.listener.maxLength = maxLength
            for image in images:
                fileExt = image.split(".")[-1]
                fileName = image.replace(("." + fileExt),"")
                if fileExt not in ok_ext:
                    ext_count = []
                    name_count = []
                    break
                else:
                    if fileExt not in ext_count:
                        ext_count.append(fileExt)
                    if fileName not in name_count:
                        name_count.append(fileName)


            if len(ext_count) == 1:
                ext = ext_count[0]
                if ext_count[0] == "tga":
                    self.ui.status_line.setText(u"找到 TGA 圖串")
                elif ext_count[0] == "tif":
                    self.ui.status_line.setText(u"找到 TIF 圖串")
                elif ext_count[0] == "png":
                    self.ui.status_line.setText(u"找到 PNG 圖串")
            elif len(ext_count) > 1 and len(name_count) > 1:
                self.ui.status_line.setText(u"資料夾內只能有一個圖串，或有其他檔案(子資料夾, Thumbs.db 除外)")
            elif len(ext_count) == 0 and len(name_count) == 0:
                self.ui.status_line.setText(u"資料夾內只能有一個圖串，或有其他檔案(子資料夾, Thumbs.db 除外)")
        else:
            self.ui.status_line.setText(u"沒有任何檔案")



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
        outputQueue.put(image)
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, output_path)
        subprocess.call(imageMagickCMD, stdout=FNULL, stderr=subprocess.STDOUT)

def worker_findMinMax(q, input_path, outputQueue):
    def findWhite(im):
        count = 0
        for count, column in enumerate(im):
            #if np.sum(column)/3/255 > 0:
            if np.sum(column, axis=0)[3] > 0:
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
    FNULL = open(os.devnull, 'w')
    sys.stdout = FNULL
    subprocess.STARTF_USESHOWWINDOW = 1
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

        flag = "-alpha set -compress zip -crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)

        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        out_path = out_dir + "/" + fileName + ".png"

        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, out_path)
        subprocess.call(imageMagickCMD.encode(sys.getfilesystemencoding()), stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        #imageMagickCMD.encode(sys.getfilesystemencoding())
        outputQueue.put(u"xx" + image)

if __name__=='__main__':
    multiprocessing.freeze_support()
    try:
        if sys.platform.startswith('win'):
            import multiprocessing.popen_spawn_win32 as forking
        else:
            import multiprocessing.popen_fork as forking
    except ImportError:
        import multiprocessing.forking as forking

    if sys.platform.startswith('win'):
        class _Popen(forking.Popen):
            def __init__(self, *args, **kw):
                if hasattr(sys, 'frozen'):
                    os.putenv('_MEIPASS2', sys._MEIPASS)
                try:
                    super(_Popen, self).__init__(*args, **kw)
                finally:
                    if hasattr(sys, 'frozen'):
                        if hasattr(os, 'unsetenv'):
                            os.unsetenv('_MEIPASS2')
                        else:
                            os.putenv('_MEIPASS2', '')
        forking.Popen = _Popen

    outputQueue = multiprocessing.Queue()
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())