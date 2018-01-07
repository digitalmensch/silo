Simply Logging
==============

Sometimes you just don't want to configure logging.


Features
--------

- Configuration using ENV variables
- Low overhead debug operation (2 op codes)
- Audit functions to track business operations
- Filter sensitive information

Configuration
-------------

.. code:: shell

    export SILO_0=syslog_format:stderr
    export SILO_1=json_format:stderr
    export DEBUG=0

Examples
--------

.. code:: python

    from silo import info, debug, audit
    
    def hello(who='World'):
        info(f'Hello, {who}!')
    
    hello()
    
    @audit(password=lambda pw: '*'*len(pw))
    def login(username, password):
        # do smart stuff here...
        raise Exception()
   
    login('duckie', 'secret')

Which will result in something looking like this:

::

    2018-01-06 09:27 INFO __main__.hello (line 2) Hello, World!
    {'timestamp': '2018-01-06T09:27:28.193821', 'level': 'INFO', 'place': '__main__.hello', 'line': 2, 'message': 'Hello, World!'}
    2018-01-06 09:31 AUDIT __main__.login Invocation of login('duckie', '******') failed with Exception()
    {'timestamp': '2018-01-06T09:31:13.836271', 'level': 'INFO', 'place': '__main__.hello', 'line': 2, 'username': 'duckie', 'password': '******', 'exception': {}}

