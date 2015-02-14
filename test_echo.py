#! /usr/bin/env python

import pytest
import sys
from echo_client import echo_client


def test_connection():
    """Test that a connect is establised by reading a returned value"""
    response = echo_client("GET test/test/test HTTP/1.1")
    print response
    assert "test/test/test" in response

def test_input():
    """Test that a none GET method returns the correct error"""
    encoded_text = u'Post test/test/test HTTP/1.1'
    response = echo_client(encoded_text)
    print response
    assert '405' in response

def test_longer_string():
    """Test that a incorrect http returns the correct error"""
    response = echo_client('GET test/test/test HTTP/1.2')
    print response
    assert '505' in response