'''
import socket
HOST=''
PORT=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print 'Connected by',addr
while 1:
	data=conn.recv(1024)
	if not data:break
	conn.sendall(data)
conn.close()
'''
#-*-coding:utf-8-*- 
import SocketServer
import sqlite3
class MyTCPHandle(SocketServer.BaseRequestHandler):
	def add(self,stuid,name,pic):

		return "Add Successfully"
	def delete(self,stuid):
		return "Delete Successfully"
	def modify(self,stuid,name=None,pic=None):
		return "Modify Successfully"
	def display(self):
		pass
	def error(self):
		pass

	def handle(self):
		#self.data=self.request.recv(1024).strip()
		request=self.request.recv(1024)
		print "{} wrote:".format(self.client_address[0])
		print "request is ",request
		method=request.split(' ')[0]
		#src=request.split(' ')[1]
		if method=='add':
			add(request.split(' ')[1],request.split(' ')[2],request.split(' ')[3])
		if method=='delete':
			delete(request.split(' ')[1])
		if method=='modify':
			modify(request.split(' ')[1],request.split(' ')[2],request.split(' ')[3])
		if method=='display':
			display()
		else:
			error()



		self.request.sendall(request.upper())

if __name__=="__main__":
	HOST,PORT="localhost",50000
	server=SocketServer.TCPServer((HOST,PORT),MyTCPHandle)
	server.serve_forever()