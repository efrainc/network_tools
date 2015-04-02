#! /usr/bin/env python

import socket
import sys

test_string = (sys.argv[-1])

def echo_client(text):
    """Initiates a socket from the client side"""

    # uncoded_text = text
    # coded_text = uncoded_text.encode('utf_8')
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(text)
    client_socket.shutdown(socket.SHUT_WR)
    text_received = ""
    done = False
    while not done:
        response = client_socket.recv(32)
        if len(response) < 32:
            done = True
        text_received = "{}{}".format(text_received, response)
    client_socket.close()
    return text_received

if __name__ == '__main__':
    echo_client(test_string)

