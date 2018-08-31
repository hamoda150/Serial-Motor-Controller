# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialMotorController.ui'
#
# Created: Sat Apr 28 04:33:01 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import serial
import image
import serial.tools.list_ports

# Declare global variables
Port = 0
duty_cycle = 0


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(825, 855)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 761, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(600, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_status = QtGui.QLabel(self.groupBox)
        self.label_status.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.label_status.setText("Status")
        # event here
        self.textEdit_status = QtGui.QTextEdit(self.groupBox)
        self.textEdit_status.setGeometry(QtCore.QRect(90, 80, 461, 81))
        self.textEdit_status.setObjectName(_fromUtf8("textEdit_status"))
        # event here
        self.lineEdit_port = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_port.setGeometry(QtCore.QRect(590, 60, 121, 22))
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        if serial_ports():
            # if port detected then automatically print it
            self.lineEdit_port.setText(serial_ports())
        else:
            # else print "Port" and the user will enter in manually
            self.lineEdit_port.setText("Port")
        
        # event here
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 501, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        # event here
        self.connect_button = QtGui.QPushButton(self.groupBox)
        self.connect_button.setGeometry(QtCore.QRect(590, 90, 121, 51))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        # connect_button with lineEdit_port
        self.connect_button.clicked.connect(self.button_click_lineEdit_port)
        # connect_button with ProgressBar
        self.connect_button.clicked.connect(self.onStart)
        self.myLongTask = TaskThread()
        self.myLongTask.taskFinished.connect(self.onFinished)
        
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 761, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        # event here
        self.forward_button = QtGui.QPushButton(self.groupBox_2)
        self.forward_button.setGeometry(QtCore.QRect(250, 130, 131, 61))
        self.forward_button.setObjectName(_fromUtf8("forward_button"))
        self.forward_button.clicked.connect(self.button_click_lineEdit_dutycycle)
        self.forward_button.clicked.connect(self.forward_button_event)
            
        # event here
        self.backward_button = QtGui.QPushButton(self.groupBox_2)
        self.backward_button.setGeometry(QtCore.QRect(250, 210, 131, 61))
        self.backward_button.setObjectName(_fromUtf8("backward_button"))
        self.backward_button.clicked.connect(self.button_click_lineEdit_dutycycle)
        self.backward_button.clicked.connect(self.backward_button_event)
              
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(270, 70, 131, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(470, 70, 201, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        # event here
        self.lineEdit_dutycycle = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_dutycycle.setGeometry(QtCore.QRect(470, 140, 191, 31))
        self.lineEdit_dutycycle.setObjectName(_fromUtf8("lineEdit_dutycycle"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 131, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        # event here
        self.start_button = QtGui.QPushButton(self.groupBox_2)
        self.start_button.setGeometry(QtCore.QRect(50, 130, 131, 61))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.start_button.clicked.connect(self.start_button_event)
        
        # event here
        self.stop_button = QtGui.QPushButton(self.groupBox_2)
        self.stop_button.setGeometry(QtCore.QRect(50, 210, 131, 61))
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.stop_button.clicked.connect(self.stop_button_event)
        
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 540, 791, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 261, 231))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(250, 60, 541, 81))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        # event here
        self.exit_button = QtGui.QPushButton(self.groupBox_3)
        self.exit_button.setGeometry(QtCore.QRect(580, 200, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Motor Controller V1.0", None))
        self.groupBox.setTitle(_translate("MainWindow", "Connection", None))
        self.label.setText(_translate("MainWindow", "Select Port", None))
        self.connect_button.setText(_translate("MainWindow", "Connect", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Controller", None))
        self.forward_button.setText(_translate("MainWindow", "Forward", None))
        self.backward_button.setText(_translate("MainWindow", "Backward", None))
        self.label_2.setText(_translate("MainWindow", "Direction", None))
        self.label_3.setText(_translate("MainWindow", "Speed (duty cycle)", None))
        self.label_4.setText(_translate("MainWindow", "Start/stop", None))
        self.start_button.setText(_translate("MainWindow", "Start", None))
        self.stop_button.setText(_translate("MainWindow", "Stop", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "About", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/image/logo.png\"/></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Coded by: Mohamed Elsamman</span></p><p><span style=\" font-size:14pt;\">Course: Automation of Mechanical Systems (ME595)</span></p></body></html>", None))
        self.exit_button.setText(_translate("MainWindow", "Exit", None))

##################################
#           labels               #
##################################
# called by this line:-
# self.connect(self.pb, SIGNAL("clicked()"),self.button_click)


# lineEdit_port
    def button_click_lineEdit_port(self):
        ##################################
        #    connecting to serial port   #
        ##################################
        global Port
        global ser
        # assign port name to global variable Port
        Port = self.lineEdit_port.text()
        ser = serial.Serial()
        ser.port = str(Port)
        ser.baudrate = 9600
        ser.open()
        self.textEdit_status.append('Connected !')
# lineEdit_dutycycle
    def button_click_lineEdit_dutycycle(self):
        global duty_cycle
        duty_cycle = self.lineEdit_dutycycle.text()
##################################
#         Forward Button         #
##################################
    def forward_button_event(self):
        print('forward button is pressed... sending 1')
        self.textEdit_status.append('forward button is pressed... sending 1')
        global ser
        global duty_cycle
        ser.write(b'1') # send number 1
        print("sending duty cycle of %d"% int(duty_cycle))
        self.textEdit_status.append("sending duty cycle of %d"% int(duty_cycle))
        ser.write(str(duty_cycle))
##################################
#         backward Button        #
##################################
    def backward_button_event(self):
        print('backward button is pressed... sending 2')
        self.textEdit_status.append('backward button is pressed... sending 2')
        global ser
        global duty_cycle
        ser.write(b'2')
        print("sending duty cycle of %d"% int(duty_cycle))
        self.textEdit_status.append("sending duty cycle of %d"% int(duty_cycle))
        ser.write(str(duty_cycle))
##################################
#          Start Bbutton         #
##################################
    def start_button_event(self):
        print('start button is pressed... sending 3')
        self.textEdit_status.append('start button is pressed... sending 3')
        global ser
        ser.write(b'3')
        ser.write(b'*')
##################################
#          Stop Bbutton          #
##################################
    def stop_button_event(self):
        print('stop button is pressed... sending 4')
        self.textEdit_status.append('stop button is pressed... sending 4')
        global ser
        ser.write(b'4')
        ser.write(b'*')

##############################################################
#                              Progress bar
# https://stackoverflow.com/questions/19442443/busy-indication-with-pyqt-progress-bar
##############################################################
    def onStart(self): 
        self.progressBar.setRange(0,0)
        self.myLongTask.start()

    def onFinished(self):
        # Stop the pulsation
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)

class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    def run(self):
        # do nothing and make the progress 100%
        self.taskFinished.emit()

        
##################################
#       get the connected serial port
##################################
def serial_ports():

    # produce a list of all serial ports. The list contains a tuple with the port number, 
    # description and hardware address
    #
    ports = list(serial.tools.list_ports.comports())  

    # return the port if 'USB' is in the description 
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

