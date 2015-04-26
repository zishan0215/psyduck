import pyaudio
import socket
import sys
import thread

def audio_init():
    """ Pyaudio Initialization """
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 10240
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True)
    return stream

def socket_init():
    """ Socket Initialization """
    # host = socket.gethostname()
    host = '10.0.0.20'
    port = 50000
    backlog = 5
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(backlog)
    return s

def socket_handler(client):
    size = 1024
    stream = audio_init()
    # Main Functionality
    while 1:
        data = client.recv(size)
        if data:
            # Write data to pyaudio stream
            stream.write(data)  # Stream the recieved audio data
            client.send('ACK')  # Send an ACK

def run():
    s = socket_init()
    while(1):
        client, address = s.accept()
        print 'Incoming connection'
        thread.start_new_thread(socket_handler, (client,))


def exit():
    client.close()
    stream.close()
    p.terminate()

if __name__=='__main__':
    run()
    exit()
