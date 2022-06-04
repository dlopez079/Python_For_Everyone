# Sockets in Python

# Python has built in support for TCP Sockets
import socket

mysock = socket.connect(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  #(host, port)