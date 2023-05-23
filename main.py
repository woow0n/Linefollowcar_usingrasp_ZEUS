import sys
import os

ap_path = os.getcwd()
sys.path.append(ap_path + "/control")
sys.path.append(ap_path + "/recognition")
sys.path.append(ap_path + "/gui")

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from gui.camera import Ui_MainWindow
from time import *
import numpy as np
import cv2
import time
import RPi.GPIO as GPIO

from ar_markers import detect_markers
from control.Raspi_MotorHAT_ import Raspi_MotorHAT, Raspi_DCMotor
from control.Raspi_PWM_Servo_Driver import PWM
from control.Raspi_Sonic import Sonic

servoDefualt = 270
servoMin = 180  # Min pulse length out of 4096
servoMax = 350 


class mythread(QThread):
    mysig = Signal(np.ndarray, list)

    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 480)
        self.cam.set(4, 320)

    def run(self):
        while True:
            ret, self.img = self.cam.read()
            if ret:
                self.printImg()
            sleep(0.1)

    def parseId(self, id):
        str_ = str(id)
        if (len(str_) == 3) & (str_[0] == 1):
            return [str_[1], str_[2]]

    def printImg(self):
        markers = detect_markers(self.img)
        coor = []
        for marker in markers:
            marker.highlite_marker(self.img)
            coor.append(marker.id)
        self.mysig.emit(self.img, coor)

    def __del__(self):
        self.quit()


class AutoRcCar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

        self.mh = Raspi_MotorHAT(addr=0x6f)
        self.myMotor = self.mh.getMotor(2)
        self.pwm = PWM(0x6F)
        self.pwm.setPWMFreq(60)
        self.flag = 0

    def main(self):
        self.th = mythread()
        self.th.mysig.connect(self.readFile)
        self.th.start()
        self.sonic = Sonic(23, 24)
        self.sonic.mysig.connect(self.listenSonic)
        self.sonic.start()

    def listenSonic(self, dist):
        self.info.setText(f"dist {dist} cm")
        if dist < 30 and self.flag:
            self.stopping()
        elif self.flag and self.myMotor.speed == 0:
            self.forwarding()
        else :
            pass

    def readFile(self, img, list_):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        pix_img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        self.screen.setPixmap(QPixmap(pix_img))
        text = '/'.join([str(ele)[1:] for ele in list_])
        # print(text)
        # self.info.setText(text)

    def closeEvent(self, event):
        self.myMotor.run(Raspi_MotorHAT.RELEASE);
        #self.pwm.setDefault()

        self.th.__del__()
        self.sonic.__del__()
        self.close()

    def forwarding(self):
        self.myMotor.start_slow(200)
        self.flag = 1

    def stopping(self):
        self.myMotor.run(Raspi_MotorHAT.RELEASE);
        self.flag = 0

    def turnleft(self):
        self.pwm.setPWM(1,0,servoMin)
    
    def turnright(self):
        self.pwm.setPWM(1,0,servoMax)



app = QApplication([])
win = AutoRcCar()
win.show()
app.exec_()
