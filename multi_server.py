# -*- coding: utf-8 -*-
import asyncore
import socket
from subprocess import call
import subprocess
import threading
import os
 
# server #####################
 
class EchoHandler(asyncore.dispatcher_with_send):
 
    def handle_read(self):
        #print(self)
        data = self.recv(256)
        if len(data) > 0:
            method = data.decode()
            print(method)

            white_list = ['ls', 'cat']
            
            try:
                p = subprocess.Popen(method, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    self.send(str(line))
                retval = p.wait()
            except:
                self.send("FAIL")
                self.close()
        else:
            print('close connect')
         
             
class SockServer(asyncore.dispatcher):
 
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(3)
 
    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            print ('connection from host: %s' % repr(addr))
            handler = EchoHandler(sock)
             
class AsyncEventLoop (threading.Thread):
 
    def run(self):
        asyncore.loop()
 
###  запуск отдельного процесса сервера из основного потока
 
server = SockServer('', 4444)
evLoop = AsyncEventLoop()
evLoop.start()