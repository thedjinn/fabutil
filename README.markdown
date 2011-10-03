# Fabutil

Fabutil is a set of helpers for Fabric deployment. This package is designed to keep the `fabfile.py` as small as possible while greatly augmenting the Fabric experience.

## Features

* Automatic indenting of nested task output
* Colored markers showing when a nested task is entered or exited
* Helper tasks for Ubuntu systems
* Helper tasks for Ruby and Rails deployments

## Installation

Just run `pip install -e git+git://github.com/thedjinn/fabutil.git`.

## Usage

This goes best with an example:

    from fabutil import *

    @task
    def foo():
        print "I'm in foo()"

    @task
    def bar():
        print "I'm in bar()"
        foo()
        print "I'm in bar() too"

As you can see this script is minimal. Fabutil handles the importing of Fabric for you so that your script only contains one import for most tasks. Of course you can still import Fabric if you wish or remove the `import *` part. This will only affect the way you access Fabutil's subtasks.

Now when we run the script we get the following output:

    $ fab bar
    >>> entering bar
      I'm in bar()
      >>> entering foo
        I'm in foo()
      >>> leaving foo
      I'm in bar() too
    >>> leaving bar

This output can be very useful in debugging complex scripts with lots of task dependencies.

Fabutil also comes with a variety of helper tasks. Consult the source code for more info about these.

## Caveats and known bugs

Fabutil only works with new-style tasks, i.e. the ones that use the `@task` decorator. Custom task classes will not yet indent properly, but this is planned for a future release.

## License

Copyright (c) 2011 Emil Loer <http://emilloer.com>

Permission  is  hereby granted, free of charge, to any person ob-
taining a copy of  this  software  and  associated  documentation
files  (the "Software"), to deal in the Software without restric-
tion, including without limitation the rights to use, copy, modi-
fy, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is  fur-
nished to do so, subject to the following conditions:

The  above  copyright  notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF  ANY  KIND,
EXPRESS  OR  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE  AND  NONIN-
FRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER  IN  AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  THE
SOFTWARE.
