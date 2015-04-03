import pyaudio
import socket
import sys
import thread

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

host = socket.gethostname()
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)



def socket_handler(socket):
    # Main Functionality
    while 1:
        data = client.recv(size)
        if data:
            # Write data to pyaudio stream
            stream.write(data)  # Stream the recieved audio data
            client.send('ACK')  # Send an ACK

while(1):
    client, address = s.accept()
    print 'Incoming connection'
    thread.start_new_thread(socket_handler, (client,))


client.close()
stream.close()
p.terminate()
