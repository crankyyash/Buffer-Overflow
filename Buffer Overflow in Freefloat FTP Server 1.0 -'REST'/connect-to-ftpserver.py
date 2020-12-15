import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	s.connect(("10.11.20.10",21))
	s.recv(1024)
	s.send("USER anonymous" + "\r\n")
	data = s.recv(1024)
	print data
	s.send("PASS test" + "\r\n")
	data = s.recv(1024)
	print data
	s.send("REST test" + "\r\n")
	data = s.recv(1024)
	print data
	s.send("QUIT" + "\r\n")
	s.close()
except:
	print "Connection error"
