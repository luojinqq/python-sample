__author__ = 'Admin'
import socket
import sys
host =''
port =8887
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
s.listen(10)
while 1:
    conn,addr = s.accept()
    print addr
    data= conn.recv(1024)
    print data
    if not data:
        break
    conn.sendall("ok")
conn.close()
