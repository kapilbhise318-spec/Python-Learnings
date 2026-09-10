import socket

b=socket.socket (socket.AF_INET, socket.SOCK_STREAM)
b.connect((socket.gethostname(), 1024))
msg=b.recv(100)
print(msg.decode("utf-8"))