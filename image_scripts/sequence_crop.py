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

'''
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/image_scripts/ui")
from PySide import QtCore, QtGui
import sequenceCropUi as sequenceCropUi
reload(sequenceCropUi)
scripts_path = "//Art-1405260002/d/assets"

import multiprocessing
import numpy as np
import os
import scipy.ndimage
import subprocess
import Queue
import threading
import datetime
import time

from PySide.QtCore import Signal as pyqtSignal
from PySide.QtCore import Slot as pyqtSlot

lock = multiprocessing.Lock()
app = QtGui.QApplication(sys.argv)

class DownloadThread(QtCore.QThread):

    data_downloaded = pyqtSignal(object)

    def __init__(self, val):
        QtCore.QThread.__init__(self)
        self.val = val

    def run(self):
        self.data_downloaded.emit(self.val)

class sequenceCrop(QtGui.QDialog):
    input_path = None
    img_count = 0
    
    def __init__(self, parent=None):
        super(sequenceCrop, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = sequenceCropUi.Ui_SequenceCrop()
        self.ui.setupUi(self)

        sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"        
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())   
        self.ui.input_folder_button.clicked.connect(self.selectFolder)
        self.ui.convert_button.clicked.connect(self.convert)
       
    def selectFolder(self):
        startingDir = 'C:/Program Files'
        dialog = QtGui.QFileDialog()
        #dialog.setOptions(QtGui.QFileDialog.DontUseNativeDialog)
        self.input_path = dialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.ui.input_path.setText(self.input_path)

    def findWhite(self, im):
        count = 0
        for count, column in enumerate(im):
            if np.sum(column)/3/255 > 0:
                break
        return count 
    
    # opens a image, runs findWhite 4 times, output result, uses multiprocess
    def findMinMax(self, image):
        input_path = self.input_path
        image = input_path + "/" + image
        im = scipy.ndimage.imread(image)
        height, width = im.shape
        y_min = findWhite(im)
        im_reverse = im[::-1]
        
        y_max = findWhite(im_reverse)
        y_max = height - y_max
        
        im = np.swapaxes(im,0,1)
        x_min = findWhite(im)
        
        im_reverse = im[::-1]
        x_max = findWhite(im_reverse)
        x_max = width - x_max
        
        lock.acquire()        
        try:
            return (x_min, x_max, y_min, y_max)
        finally:        
            lock.release()
    
    # uses multithreading and queue
    def cropImage(self, q):
        while True:
            image = q.get()
            in_path = input_path + "/" + image
            out_dir = input_path + "/cropped"
            fileName, fileType = image.split(".")
                
            flag = "-compress zip -crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)
            if os.path.isdir(out_dir) == False:
                os.makedirs(out_dir)
            out_path = out_dir + "/" + fileName + ".tif"
            
            imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
            subprocess.call(imageMagickCMD)
            q.task_done()

    def convertTga(self, q):
        while True:
            image = q.get()
            input_path = self.ui.input_path.text()
            in_path = input_path + "/" + image
            out_dir = input_path + "/tmp"
            fileName, fileType = image.split(".")
                
            flag = "-compress zip"
            if os.path.isdir(out_dir) == False:
                os.makedirs(out_dir)
            out_path = out_dir + "/" + fileName + ".tif"

            imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
            subprocess.call(imageMagickCMD)
            q.task_done() 

            val = 100 - int(float(q.qsize())/float(self.img_count) * 100)
            print val

            downloader = DownloadThread(val)
            downloader.data_downloaded.connect(self.on_data_ready)
            downloader.start()            
            
            
    def on_data_ready(self, val):
        print val
        self.ui.progress_bar.setValue(val)
        
    def buildQueue(self, images):
        for image in images:
            image = input_path + "/" + image
            q.put(image)
        return q
        
    def start_process():
        print 'Starting', multiprocessing.current_process().name        
        
    def convert(self):
        self.ui.convert_button.setVisible(0)
        self.ui.progress_bar.setVisible(1)

        global x_size, y_size, x_min, y_min, x_max, y_max
        input_path = self.ui.input_path.text()
        
        input_path = r"d:/sequence"
        images = [f for f in os.listdir(input_path) if os.path.isfile(input_path + "/" + f)]
        images = images[0:77]
        self.img_count = len(images)

        ext_count = []
        for image in images:
            fileName, fileExt = image.split(".")
            if fileExt not in ext_count:
                ext_count.append(fileExt)
        if len(ext_count) == 1:
            ext = ext_count[0]
        if ext == 'tga':
            q = ""
            q = Queue.Queue(maxsize = 0)
            for image in images:
                q.put(image)            
            #self.convertTga(q)

            workers = []
            for x in range(3):
                worker = threading.Thread(target=self.convertTga, args=(q,))
                worker.setDaemon(True)
                worker.start()
                app.processEvents() 
            for worker in workers:
                worker.join()
            q.join()            

        '''
        images = [x for x in os.listdir(input_path) if 'tif' in x]
    
        im = scipy.ndimage.imread(input_path + "/" + images[0])
        height, width = im.shape    
        
        x_min, x_max, y_min, y_max = findMinMax(images[0])
    
        now = datetime.datetime.now()
        pool = multiprocessing.Pool(processes=12, initializer=start_process,) # run no more than 6 at a time
        outputs = pool.map(findMinMax, images) # pass full list (12 items)
        pool.close()
        pool.join()
    
        diff = datetime.datetime.now() - now
        #print "findMinMax executed in " + str(diff)
        now = datetime.datetime.now()
    
        for output in outputs:
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
        
        q = ""
        q = Queue.Queue(maxsize = 0)
        for image in images:
            q.put(image)

        for x in range(8):
            worker = threading.Thread(target=cropImage, args=(q,))
            worker.setDaemon(True)
            worker.start()
        q.join()
        diff = datetime.datetime.now() - now
        #print "cropImage executed in " + str(diff) 
        '''
if __name__ == '__main__':
    widget = sequenceCrop()
    widget.show()
    sys.exit(app.exec_())

