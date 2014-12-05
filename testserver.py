#-*-coding:utf-8-*- 
import SocketServer
import sqlite3
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
conn=sqlite3.connect("namelist.db")

class MyTCPHandle(SocketServer.BaseRequestHandler):
	#以下为该类HTTP协议支持的方法
	def add(self,stuid,name,picture=None):
		curadd=conn.cursor()
		curadd.execute("insert into stu values(?,?,?)",(stuid,name,picture,))
		conn.commit()
		return "Add Successfully"

	def delete(self,stuid):
		curdel=conn.cursor()
		curdel.execute("delete * from stu where stuid=?",(stuid,))
		conn.commit()
		return "Delete Successfully"

	def modify(self,stuid,name=None,picture=None):
		curmod=conn.cursor()
		curmod.execute("update stu set name=?,picture=? where stuid=?",(name,picture,stuid,))
		conn.commit()
		return "Modify Successfully"

	def display(self):
		curls=conn.cursor()
		curls.execute("select stuid,name,picture from stu")
		result=curls.fetchall()
		return result


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