#-*-coding:utf-8-*- 
import socket
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

#HOST,PORT='localhost',50000
PORT=50000
HOST=raw_input('Please input the server IP: ')
print "Now connecting to server."
while(True):
	#data=" ".join(sys.argv[1:])
	data=raw_input("Please input your instruction:")
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		sock.connect((HOST,PORT))
		sock.sendall(data)
		received=sock.recv(1024)
	finally:
		sock.close()
	print "Sent: {}".format(data)
	print "Received:\n{}".format(received)
	#if data=="quit":