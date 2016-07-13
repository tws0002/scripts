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
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 14:34:40 2016

@author: julio
"""
import sys
import multiprocessing
import os
import subprocess
from functools import partial
import threading
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/image_scripts/ui")
from PySide import QtCore, QtGui

import scipy.ndimage
import numpy as np


import sequenceCropUi as sequenceCropUi
import Queue
import datetime
import time
reload(sequenceCropUi)
scripts_path = "//Art-1405260002/d/assets"

class sequenceCrop(QtGui.QDialog):
    POISON_PILL = "STOP"

    def __init__(self, parent=None):
        global queue1
        global queue2
        
        
        super(sequenceCrop, self).__init__(parent)
        self.progressBarCurrentValue=0
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = sequenceCropUi.Ui_SequenceCrop()
        self.ui.setupUi(self)
        sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())
        self.ui.input_folder_button.clicked.connect(self.selectFolder)
        #self.ui.input_path.setText("d:/sequence")
        self.ui.input_path.textChanged.connect(self.setOutput)
        self.ui.closeEvent = self.closeEvent        
        self.ui.progress_bar.setValue(0)
        #self.ui.progress_bar.hide()
        self.maxLength = 100
        self.count = 0
        self.listening = True
        self.workType = ""
        self.ui.convert_button.clicked.connect(self.convert)
        self.thread = threading.Thread(target=self.progressListener)
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()    

    def setOutput(self):
        input_path = self.ui.input_path.text()
        output_path = input_path + "/cropped"
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            sys.exit(app.exec_())
        else:
            event.ignore()
        
    def buildQueue(self, images):
        q = multiprocessing.Queue()
        for image in images:
            q.put(image)
        q.put(self.POISON_PILL)        
        return q

    def selectFolder(self):
        startingDir = 'C:/Program Files'
        dialog = QtGui.QFileDialog()
        #dialog.setOptions(QtGui.QFileDialog.DontUseNativeDialog)
        self.input_path = dialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.ui.input_path.setText(self.input_path)

    def convert(self):
        global x_size, y_size, x_min, y_min, x_max, y_max
        input_path = self.ui.input_path.text()
        images = [f for f in os.listdir(input_path) if os.path.isfile(input_path + "/" + f)]
        images = images[0:10]
        self.maxLength = len(images)
        self.ui.progress_bar.setMaximum(self.maxLength)        
        imagesQ = self.buildQueue(images)    
        
        ext_count = []
        for image in images:
            fileName, fileExt = image.split(".")
            if fileExt not in ext_count:
                ext_count.append(fileExt)
        if len(ext_count) == 1:
            ext = ext_count[0]
        if ext == "tga":
            jobs = []
            for x in range(8):
                try:
                    self.worker = multiprocessing.Process(target=worker_tga, args=(imagesQ, input_path, self.maxLength, queue1))
                    self.worker.daemon = True
                    jobs.append(self.worker)
                    self.worker.start()
                except EOFError:
                    break
                except:
                    pass
            for job in jobs:
                job.join()
            
            ### point input path and rebuild images
            self.count = 0            
            input_path = input_path + "/tmp"
            images = [f for f in os.listdir(input_path) if os.path.isfile(input_path + "/" + f)]
            images = images[0:10]
            imagesQ = self.buildQueue(images)    

        #Find min max
        im = scipy.ndimage.imread(input_path + "/" + images[0])
        height, width, channel = im.shape    
        
        jobs = []
        for x in range(12):
            try:
                self.worker = multiprocessing.Process(target=worker_findMinMax, args=(imagesQ, input_path, self.maxLength, queue1))
                self.worker.daemon = True
                jobs.append(self.worker)
                self.worker.start()
            except EOFError:
                break
            except:
                pass
        for job in jobs:
            job.join()        

        #Cropping
        self.count = 0
        input_path = self.ui.input_path.text()
        images = [f for f in os.listdir(input_path) if os.path.isfile(input_path + "/" + f)]
        images = images[0:10]
        imagesQ = self.buildQueue(images)
        
        jobs = []
        for x in range(8):
            try:
                self.worker = multiprocessing.Process(target=worker_crop, args=(imagesQ, input_path, queue1, x_size, y_size, x_min, y_min))
                self.worker.daemon = True
                jobs.append(self.worker)
                self.worker.start()
            except EOFError:
                break
            except:
                pass
        for job in jobs:
            job.join()        



    def updateProgress(self, current):
        self.ui.progress_bar.setValue(current)
        QtGui.qApp.processEvents()

    def progressListener(self):
        global queue1
        global x_size, y_size, x_min, y_min, x_max, y_max
        outputs = []
        """ Method that runs forever """
        while self.listening == True:
            x = queue1.get()
            if type(x) == unicode:
                self.count = self.count + 1
                perc = ((float(self.count) / float(self.maxLength)) * 100)
                print str(perc) + "%"            
                #self.updateProgress(self.count) 
                self.ui.status_line.setText(x)

            if type(x) == list:
                self.ui.status_line.setText(u"計算範圍中....")
                outputs.append(x)
                self.count = self.count + 1
                perc = ((float(self.count) / float(self.maxLength)) * 100)
                print str(perc) + "%"  
                self.updateProgress(self.count)
                if self.count == self.maxLength:
                    x_min, x_max, y_min, y_max = outputs[0]
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
 
def worker_tga(q, input_path, maxLength, returnQ):
    while True:
        try:
            image = q.get(block=True, timeout=0.1)

        except Queue.Empty: # Queue here refers to the  module, not a class
            break

        if image == "STOP":
            break        

        out_dir = input_path + "/tmp"
        image_path = input_path + "/" + image

        fileName, fileType = image.split(".")
    
        flag = "-compress zip"
        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        output_path = out_dir + "/" + fileName + ".tif"

        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, output_path)
        subprocess.call(imageMagickCMD)

        returnQ.put(u"轉 TIF " + image)
    q.close()

def worker_crop(q, input_path, returnQ, x_size, y_size, x_min, y_min):
    while True:
        try:
            image = q.get(block=True, timeout=0.1)

        except Queue.Empty: # Queue here refers to the  module, not a class
            break

        if image == "STOP":
            break  

        out_dir = input_path + "/cropped"
        image_path = input_path + "/" + image

        fileName, fileType = image.split(".")
        print (x_size, y_size, x_min, y_min)
            
        flag = "-alpha on -compress zip -crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)

        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        out_path = out_dir + "/" + fileName + ".tif"
        
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_path, flag, out_path)            
        subprocess.call(imageMagickCMD)

        returnQ.put(u"裁切圖檔 " + image)
    q.close()


def worker_findMinMax(q, input_path, maxLength, returnQ):
    def findWhite(im):
        count = 0
        for count, column in enumerate(im):
            if np.sum(column)/3/255 > 0:
                break
        return count 

    while True:
        try:
            image = q.get(block=True, timeout=0.1)
        except Queue.Empty: # Queue here refers to the  module, not a class
            break

        if image == "STOP":
            #print "All Done!"
            break        

        #input_path = input_path + "/" + image
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
        
        returnQ.put([x_min, x_max, y_min, y_max])

# 4 thread 0:00:30.188000
# 8 thread 0:00:23.576000
# 10 thread 0:00:22.123000
# 12 thread 0:00:22.275000
   
if __name__ == '__main__':
    queue1 = multiprocessing.Queue()
    app = QtGui.QApplication([])
    win = sequenceCrop()
    win.show()

    sys.exit(app.exec_())


