'''
import socket
HOST='localhost'
PORT=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall('Hello,world')
data=s.recv(1024)
s.close()
print 'Received',repr(data)
'''
#-*-coding:utf-8-*- 
import socket
import sys

HOST,PORT='localhost',50000
data=" ".join(sys.argv[1:])
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	sock.connect((HOST,PORT))
	sock.sendall(data+"\n")
	received=sock.recv(1024)
finally:
	sock.close()

print "Sent: {}".format(data)
print "Received: {}".format(received)