import inspect
import sys
#
#
class Hi:
    def __init__(self):
        self.fileName = inspect.stack()[1][1]
        self.line = inspect.stack()[1][2]
        self.method = inspect.stack()[1][3]

    def raiseNotDefined(self):
        return self.method
        # print("*** Method not implemented: %s at line %s of %s" % (self.method, self.line, self.fileName))
        # sys.exit(1)

# Helo = Hi()
# print(Helo.raiseNotDefined())
#
# import inspect
# import sys
#
# class hi:
#     def raiseNotDefined(self):
#         fileName = inspect.stack()[1][1]
#         line = inspect.stack()[1][2]
#         method = inspect.stack()[1][3]
#         print(fileName)
#         print(line)
#         print(method)
#             # print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
#         sys.exit(1)
#
#
# class hello:
#     def __init__(self):
#         self.__init__()
#
