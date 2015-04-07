import pyaudio
import socket
import sys
import time
from PyQt4 import QtGui, QtCore, uic
import sys

# Pyaudio Initialization
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

# Socket Initialization
# host = socket.gethostname()
host = '10.0.0.9'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
#
# #window
# class Window(QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#         self.resize(250, 350)
#         self.move(700, 300)
#         self.setWindowTitle('Client')
#         self.button = QtGui.QPushButton('Call', self)
#         self.button.clicked.connect(self.handleButton)
#         layout = QtGui.QVBoxLayout(self)
#         layout.addWidget(self.button)
#
#     def handleButton(self):
#         while 1:
#             data = stream.read(chunk)
#             s.send(data)
#             s.recv(size)
#
# # Main Functionality
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#
#     w = Window()
#     w.show()
#     sys.exit(app.exec_())

while 1:
    data = stream.read(chunk)
    s.send(data)
    s.recv(size)

s.close()
stream.close()
p.terminate()
