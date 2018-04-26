import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9998

s.connect((host, port))

tm = s.recv(1024)

s.close()
