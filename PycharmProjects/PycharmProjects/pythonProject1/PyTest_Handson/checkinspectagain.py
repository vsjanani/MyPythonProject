import inspect


# def hi():
#     print(inspect.stack()[1][3])
#
# def foo():
#     hi()
#
# foo()


class main:
    def __init__(self):
        self.method = inspect.stack()[1][3]
        
    def checkprint(self):
        print(self.method)

class hi:
    def mycheck(self):
        check = main()
        check.checkprint()

doo = hi()
doo.mycheck()