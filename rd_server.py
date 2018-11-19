# -*- coding: utf-8 -*-
import os
import socket

HOST = "localhost"
PORT = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
client, addr = s.accept()


try:
    cmd = s.recv(1024)
    print cmd
except:
    print "asdasd"

"""
try:
    os.system(cmd)
    client.sendall("OK")
except:
    client.sendall("FAIL")
    client.close()

"""