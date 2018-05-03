import socket

host = ''
port = 60000

s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('server lis')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by '+ str(addr))
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close() 