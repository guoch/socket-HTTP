#-*-coding:utf-8-*- 
import socket
import sys
import struct
reload(sys) 
sys.setdefaultencoding('utf-8')

address = ('localhost', 50000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

messages = ["foobar", "barbaz", "bazquxfad", "Jimmy Carter"]

for s in messages:

    totallen = len(s) 
    pack1 = struct.pack('>I', totallen) # the first part of the message is length
    client_socket.sendall(pack1)
    client_socket.sendall(s)