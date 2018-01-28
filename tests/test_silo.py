import pytest
import silo

def test_functions_return_none():
    assert emergency('silo test message') == None
    assert alert('silo test message') == None
    assert critical('silo test message') == None
    assert error('silo test message') == None
    assert warning('silo test message') == None
    assert notice('silo test message') == None
    assert info('silo test message') == None
    assert debug('silo test message') == None
