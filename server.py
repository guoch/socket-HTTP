#-*-coding:utf-8-*- 
import SocketServer
import sqlite3
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
conn=sqlite3.connect("namelist.db")
#定义类HTTP协议支持的方法

#在学生名单中添加数据
def add(stuid,name,picture=None):
	curadd=conn.cursor()
	curadd.execute("insert into stu values(?,?,?)",(stuid,name,picture,))
	conn.commit()
	return "Add Successfully"

#在学生名单中删除数据
def delete(stuid):
	curdel=conn.cursor()
	curdel.execute("delete from stu where stuid=?",(stuid,))
	conn.commit()
	return "Delete Successfully"

#在学生名单中修改数据
def modify(stuid,name,picture=None):
	curmod=conn.cursor()
	curmod.execute("update stu set name=?,picture=? where stuid=?",(name,picture,stuid,))
	conn.commit()
	return "Modify Successfully"

def ls():
	curls=conn.cursor()
	curls.execute("select stuid,name,picture from stu")
	result=curls.fetchall()
	dis=""
	for line in result:
		dis=dis+str(line[0])+"\t"+str(line[1])+"\t"+str(line[2])+"\n"
	return dis
	#dis=str(result)
	#return dis

def error():
	return "The server cannot process your request,Maybe some error"

class GchHttpHandle(SocketServer.BaseRequestHandler):
	#以下为该类HTTP协议支持的方法
	def handle(self):
		#self.data=self.request.recv(1024).strip()
		request=self.request.recv(1024)
		print "{} wrote:".format(self.client_address[0])
		print "request is ",request
		method=request.split(' ')[0]
		backmessage=""
		#src=request.split(' ')[1]
		print request.split(' ')
		if method=='add':
			if len(request.split(' '))<4:
				backmessage=add(request.split(' ')[1],request.split(' ')[2])
			else:
				backmessage=add(request.split(' ')[1],request.split(' ')[2],request.split(' ')[3])
		elif method=='delete':
			backmessage=delete(request.split(' ')[1])
		elif method=='modify':
			if len(request.split(' '))<4:
				backmessage=modify(request.split(' ')[1],request.split(' ')[2])
			else:
				backmessage=modify(request.split(' ')[1],request.split(' ')[2],request.split(' ')[3])
		elif method=='ls':
			backmessage=ls()
		else:
			backmessage=error()
		self.request.sendall(backmessage)

#在主函数中实例化类，制定server端的服务器和端口号，本程序中默认端口号为50000
if __name__=="__main__":
	HOST,PORT="localhost",50000
	server=SocketServer.TCPServer((HOST,PORT),GchHttpHandle)
	server.serve_forever()