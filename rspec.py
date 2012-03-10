import re
import sys
import inspect
from colors import red, green


DEBUG = False
current_function = ""


class Opinion(object):

    def __init__(self, thing):
        self.thing = thing
        self.args = []
        self.kwargs = {}

    def should(self, matcher):
        if not inspect.getargspec(matcher).args:
            matcher = matcher()

        try:
            matcher(self.thing, *self.args, **self.kwargs)
        except AssertionError as e:
            print(red("".join([current_function, " failed: ", str(e)])))
        else:
            print(green(current_function))

        return self

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self


def tracer(frame, event, arg):
    if DEBUG and event == 'call':
        print(event, frame, arg, frame.f_code.co_name, frame.f_globals.keys())

    for name, function in frame.f_globals.items():
        if callable(function) and function.__module__ == "__main__":
            frame.f_globals[name] = Opinion(function)

    return tracer


def rspec_run(function):
    global current_function
    ptrace = sys.gettrace()

    try:
        sys.settrace(tracer)
        current_function = re.sub("_", " ", function.__name__)
        function()
    finally:
        sys.settrace(ptrace)
