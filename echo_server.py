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

    try:
        while True:
            done = False
            text_received = ''
            while not done:
                conn, addr = server_socket.accept()
                response = conn.recv(32)
                if len(response) < 32:
                    done = True
                text_received = "{}{}".format(text_received, response)
            conn.sendall(text_received)
    except KeyboardInterrupt:
       server_socket.close()


if __name__ == '__main__':
    echo_server()