import socket
import sys
import struct

address = ('localhost', 6005)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(address)

while True:
    print "Listening"

    totallen = server_socket.recv(4)
    totallenRecv = struct.unpack('>I', totallen)[0]

    message = server_socket.recv(totallenRecv)

    print message