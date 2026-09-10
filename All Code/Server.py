import  socket
a=socket.socket (socket.AF_APPLETALK, socket.SOCK_STREAM)
a.bind((socket.gethostname(), 1042))

while True:
    clt,addr=a.accept()
    print(f"Connection Established{addr}")
    clt.send(bytes("Network progamming using Python","utf-8"))
