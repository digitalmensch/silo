import silo

def test_functions_return_none():
    assert silo.emergency('silo test message') == None
    assert silo.alert('silo test message') == None
    assert silo.critical('silo test message') == None
    assert silo.error('silo test message') == None
    assert silo.warning('silo test message') == None
    assert silo.notice('silo test message') == None
    assert silo.info('silo test message') == None
    assert silo.debug('silo test message') == None
