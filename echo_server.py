#! /usr/bin/env python

import socket

def echo_server():
    """Initiates a socket from the server side"""
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    server_socket.bind(('127.0.0.1', 50000))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    text = conn.recv(32)
    print text
    conn.sendall("Yes, I hear you.")
    conn.close()


if __name__ == '__main__':
    echo_server()