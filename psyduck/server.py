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
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()

# Main Functionality
while 1:
    data = client.recv(size)
    
    if __name__ == '__main__':
		app = QtGui.QApplication(sys.argv)
		app.setStyle("cleanlooks")

		listwidget = QtGui.QListWidget()
		listwidget.show()

		if data:
        	#Write data to pyaudio stream
	        stream.write(data)  # Stream the recieved audio data
	        client.send('ACK')  # Send an ACK

		sys.exit(app.exec_())

client.close()
stream.close()
p.terminate()

