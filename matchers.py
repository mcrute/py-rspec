def equal(expected):
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert actual == expected, "%r != %r" % (actual, expected)

    return tester


def be_none():
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert actual is None, "%r is not None" % actual

    return tester


def be_true():
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert actual is True, "%r is not True" % actual

    return tester


def be_false():
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert actual is False, "%r is not False" % actual

    return tester


def be_a(expected):
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert isinstance(actual, expected), "%r is not a %r" % (actual, expected)

    return tester


def be(expected):
    def tester(function, *args, **kwargs):
        actual = function(*args, **kwargs)
        assert actual is expected, "%r is not %r" % (actual, expected)

    return tester


def raise_exception(expected):
    def tester(function, *args, **kwargs):
        try:
            function(*args, **kwargs)
        except expected:
            pass
        else:
            raise AssertionError("%s not raised" % expected)

    return tester
