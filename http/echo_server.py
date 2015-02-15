#! /usr/bin/env python

import socket
import email.utils
import os
import sys
import mimetypes


def echo_servers():
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
            if text_received:
                response_user = parase_request(text_received)
            conn.sendall(response_user)
    except KeyboardInterrupt:
       server_socket.close()

def response_ok(content, body_text):
    first_line = 'HTTP/1.1 200 OK'
    timestamp = 'Date: ' + email.utils.formatdate(usegmt=True)
    header = 'Content-Type: {}'.format(content)
    body = body_text
    size = str(sys.getsizeof(body))
    end = '\r\n'
    response = [first_line, timestamp, header, size, body, end]
    return end.join(response)

def response_error(error_code, error_message):
    first_line = 'HTTP/1.1 {} {}'.format(error_code, error_message)
    timestamp = 'Date: ' + email.utils.formatdate(usegmt=True)
    header = 'Content-Type: text/plain'
    body = '{} {}'.format(error_code, error_message)
    size = str(sys.getsizeof(body))
    end = '\r\n'
    error_response = [first_line, timestamp, header, size, body, end]
    return end.join(error_response)

def parase_request(client_request):
    full_text = client_request.splitlines()
    first_line = full_text[0].split(' ')
    response = error_determination(first_line)
    return response

def error_determination(http_methods):

    if http_methods[0] != 'GET':
        error = response_error('405', 'Method Not Allowed')
        return error
    elif http_methods[2] != 'HTTP/1.1':
        error = response_error('505', 'HTTP Version Not Supported')
        return error
    else:
        return resolve_uri(http_methods[1])

def resolve_uri(uri):
    if os.path.isdir(os.path.abspath(uri)):
        list_of_files = dir_list(uri)
        response = response_ok('text/html', list_of_files)
        return response
    elif os.path.isfile(uri):
        file_info = file_text(uri)
        content = mimetypes.guess_type(uri)[0]
        response = response_ok(content, file_info)
        return response
    else:
        return response_error('404', 'Content Not Found')

def file_text(uri):
    file_information = open(uri, "r")
    body = file_information.read()
    file_information.close()
    return body

def dir_list(uri):
    dir_list = ""
    for i in os.listdir(uri):
        dir_list += "<li>"+i+"</li>\n"
    body = "<ul>\n{}</ul>\n".format(dir_list)
    return body

if __name__ == '__main__':
    echo_servers()