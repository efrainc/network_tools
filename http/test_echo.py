#! /usr/bin/env python

import pytest
import os
from echo_client import echo_client


def test_connection():
    """Test that a connect is establised by reading a the OK value"""
    response = echo_client("GET webroot/sample.txt HTTP/1.1")
    print response
    assert "HTTP/1.1 200 OK" in response

def test_input():
    """Test that a none GET method returns the correct error"""
    encoded_text = u'Post test/test/test HTTP/1.1'
    response = echo_client(encoded_text)
    assert '405' in response

def test_longer_string():
    """Test that a incorrect http returns the correct error"""
    response = echo_client('GET test/test/test HTTP/1.2')
    assert '505' in response

"""
Updated Tests for http2 branch
"""

def test_dir_query():
    """Test that the contens of a directory are properly returned"""
    response = echo_client("GET webroot/ HTTP/1.1")
    list_of_items = os.listdir('webroot')
    for item in list_of_items:
        assert item in response

def test_error404():
    """Test that a request for a faulty uri returns a 404 error"""
    response = echo_client("GET test/test HTTP/1.1")
    assert '404' in response

def test_read_file():
    """Test that a request for a .txt file will return the file contens"""
    response = echo_client("GET webroot/sample.txt HTTP/1.1")
    test_file = open('webroot/sample.txt', 'r')
    body = test_file.read()
    line_by_line = body.splitlines()
    test_file.close()
    for item in line_by_line:
        assert item in response


