#!/usr/bin/env python
# coding: utf-8

import socket
import thread


# Simple socket server that responds to incoming messages
class Server:

    HOST = ''
    PORT = 8888
    CONNECTIONS = 10

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((Server.HOST, Server.PORT))
        self.socket.listen(Server.CONNECTIONS)

    # Handles concurrent connections
    def thread(self, conn):

        conn.send("Welcome! Type something and hit enter\n")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            reply = ("Hi %s" % (data))
            conn.sendall(reply)

        conn.close()

    # Blocking call that listens indefintely for incoming connections
    def listen(self):

        print ("Listening On: %s:%s" % (Server.HOST, Server.PORT))
        print "Connect via 'telnet localhost 8888'"

        while True:
            conn, addr = self.socket.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            thread.start_new_thread(self.thread, (conn,))

        self.socket.close()

if __name__ == "__main__":
    server = Server()
    server.listen()
