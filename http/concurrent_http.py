#! /usr/bin/env python

import email.utils
import os
import sys
import mimetypes
from echo_server import (
    parase_request,
    error_determination,
    response_error,
    resolve_uri,
    dir_list,
    file_text,
    response_ok
)


def concurrent_server(socket, address):
    """Initiates a socket from the server side"""
    text_received = ''
    done = False
    while not done:
        response = socket.recv(32)
        if len(response) < 32:
            done = True
        text_received = "{}{}".format(text_received, response)
    if text_received:
        response_user = parase_request(text_received)
        socket.sendall(response_user)
    socket.close()


def start():
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 50000), concurrent_server)
    print('Starting http server on port 50000')
    server.serve_forever()

if __name__ == '__main__':
    start()