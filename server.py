#-*-coding:utf-8-*- 
import socket
import sys
import struct
reload(sys) 
sys.setdefaultencoding('utf-8')

address = ('localhost', 50000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)

while True:
    print "Listening"

    totallen = server_socket.recv(4)
    totallenRecv = struct.unpack('>I', totallen)[0]

    message = server_socket.recv(totallenRecv)

    print message