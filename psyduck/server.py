import pyaudio
import socket
import sys
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
                output = True)

# Socket Initialization
host = ''
port = 50002
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()

#window
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(250, 350)
        self.move(200, 300)
        self.setWindowTitle('Server')
        data = client.recv(size)
        if data:
            self.button = QtGui.QPushButton('Disconnect', self)
            self.button.clicked.connect(self.disconnectCall)
            layout = QtGui.QVBoxLayout(self)
            layout.addWidget(self.button)
            self.button = QtGui.QPushButton('Attend', self)
            self.button.clicked.connect(self.attendCall)
            layout = QtGui.QVBoxLayout(self)
            layout.addWidget(self.button)

    def attendCall(self):
        while 1:            
            data = client.recv(size)
            if data:
                #Write data to pyaudio stream
                stream.write(data)  # Stream the recieved audio data
                client.send('ACK')  # Send an ACK
                self.button = QtGui.QPushButton('Disconnect', self)
                layout = QtGui.QVBoxLayout(self)
                layout.addWidget(self.button)
                
            elif self.button.clicked():
                self.button.clicked.connect(self.disconnectCall)
                
    def disconnectCall(self):
        self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent)

    def closeEvent(self,event):
        print "Disconnecting..."
        self.deleteLater()
        event.accept()
        
        
# Main Functionality
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()
    
    sys.exit(app.exec_())

client.close()
stream.close()
p.terminate()

