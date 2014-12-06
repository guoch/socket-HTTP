#-*-coding:utf-8-*- 
import socket
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

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