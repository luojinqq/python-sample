import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print msg
	sys.exit()
host = 'localhost'
port = 8887

ip = socket.gethostbyname(host)
print ip

s.connect((ip, port))

message = "GET http://www.baidu.com/ HTTP/1.1\r\n\
                Accept: html/text\r\n\
                Host: 220.181.6.175:80\r\n\
                Connection: Close\r\n\r\n"

s.sendall(message)

reply = s.recv(4096)
print reply
