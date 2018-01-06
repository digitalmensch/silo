Simply Logging
==============

Sometimes you just don't want to configure logging first or decide between
human readable and structured.

::

    >>> from silo import info, debug, audit
    >>> def hello(who='World'):
    ...     info(f'Hello, {who}!')
    ...
    >>> hello()
    2018-01-06 09:27 INFO __main__.hello (line 2) Hello, World!
    {'timestamp': '2018-01-06T09:27:28.193821', 'level': 'INFO', 'place': '__main__.hello', 'line': 2, 'message': 'Hello, World!'}
    >>>

Unless the application was started with debugging output enabled, debug is set
to a dummy method with overhead low.

::

    >>> from dis import dis
    >>> dis.dis(debug)
      2           0 LOAD_CONST               0 (None)
                  2 RETURN_VALUE
    >>> # ...unless the environment variable DEBUG is truthy
    >>>

Sometimes function invocations need to be logged for business reasons.

::

    >>> @audit(password=lambda pw: '*'*len(pw))
    ... def login(username, password):
    ...     # do smart stuff here...
    ...     raise Exception()
    ...
    >>> login('duckie', 'secret')
    2018-01-06 09:31 AUDIT __main__.login Invocation of login('duckie', '******') failed with Exception()
    {'timestamp': '2018-01-06T09:31:13.836271', 'level': 'INFO', 'place': '__main__.hello', 'line': 2, 'username': 'duckie', 'password': '******', 'exception': {}}
    >>>
