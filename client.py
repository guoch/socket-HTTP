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
	print '''支持指令：\n
	列出指令 ls :   如 "ls" 列出名单中学生所有信息 \n
	添加指令 add：  如 "add 112433 Chenghao D:\chenghao.jpg" 在名单中添加学号为112433 姓名为Chenghao 图片为chenghao.jpg\n
	删除指令 delete 如 "delete 112433"  在名单中删除学号为112433学生的记录\n
	修改指令 modify 如 "modify 112433 Guochenghao" 把学号为112433的学生姓名改为 Guochenghao\n '''
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