import os

# Make sure that greetings method is accessible from shell
class Foo(object):
    def greetings(self):
        print 'Hello, World!'

os.environ['PYTHONINSPECT'] = 'True'