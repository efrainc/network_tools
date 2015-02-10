#! /usr/bin/env python

import pytest
import sys
from echo_client import echo_client
from echo_server import echo_server

def test_connection():
    """Test that a connect is establised by reading a returned value"""
    assert "test" == echo_client("test")

def test_input():
    """Test that a unicode imput returns correctly"""
    encoded_text = u'kjfk'
    assert 'kjfk' == echo_client(encoded_text)

def test_longer_string():
    """Test that a string over 32 bytes gets read correctly"""
    print sys.getsizeof('aklsjflksjflkasjflsjfl')
    assert 'aklsjflksjflkasjflsjfl' == echo_client('aklsjflksjflkasjflsjfl')

