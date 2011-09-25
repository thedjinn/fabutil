import sys
from types import MethodType

class Indenter:
    # TODO: use __future__.print_function

    def __init__(self, stream):
        self.stream = stream
        self.lf = True
        self.skip = False
        self.depth = 0

    def push(self):
        print "\001"

    def pop(self):
        print "\002"

    def write(self, data):
        for c in data:
            if self.skip:
                self.skip = False
                continue

            if ord(c) == 1:
                self.depth += 1
                self.skip = True
            elif ord(c) == 2:
                self.depth -= 1
                self.skip = True
            else:
                if self.lf:
                    self.stream.write(self.depth * "  ")
                    self.lf = False

                if (ord(c) == 10) or (ord(c) == 13):
                    self.lf = True

                self.stream.write(c)

    def __getattr__(self, aname):
        target = self.stream
        f = getattr(target, aname)
        if isinstance(f, MethodType):
            return new.instancemethod(f.im_func, self, target.__class__)
        else:
            return f

indenter = Indenter(sys.stdout)
sys.stdout = indenter

__all__ = ["indenter"]
