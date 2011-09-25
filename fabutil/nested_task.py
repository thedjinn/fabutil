from fabric.colors import green
import fabric.tasks as tasks
from types import MethodType

from indenter import indenter

def task(*args, **kwargs):
    func, args = args[0], ()

    def myrun(self, *args, **kwargs):
        print green(">>> entering ") + green("%s" % func.__name__, True)
        indenter.push()
        self.oldrun(*args, **kwargs)
        indenter.pop()
        print green(">>> leaving ") + green("%s" % func.__name__, True)

    def wrapper(func):
        t = tasks.WrappedCallableTask(func, *args, **kwargs)
        t.oldrun = t.run
        t.run = MethodType(myrun, t, tasks.WrappedCallableTask)
        return t

    return wrapper(func)

tasks.task = task

__all__ = ["task"]
