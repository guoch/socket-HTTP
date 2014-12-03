import socket
import sys
import struct

address = ('localhost', 6005)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(address)

messages = ["foobar", "barbaz", "bazquxfad", "Jimmy Carter"]

for s in messages:

    totallen = len(s) 
    pack1 = struct.pack('>I', totallen) # the first part of the message is length
    client_socket.sendall(pack1)
    client_socket.sendall(s)