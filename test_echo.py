#! /usr/bin/env python

import pytest
from echo_client import echo_client
from echo_server import echo_server

# def test_connection():
#     """Test that a connect is establised by reading a returned value"""
#     a = echo_client("test")
#     assert "Yes, I hear you." == a

def test_input():
    """Test that a unicode imput returns correctly"""
    encoded_text = u'kjfk'
    b = echo_client(encoded_text)
    assert "Yes, I hear you." == b
