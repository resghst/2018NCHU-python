import socket
import time 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9998

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()
    print("%s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    print str(currentTime)
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()