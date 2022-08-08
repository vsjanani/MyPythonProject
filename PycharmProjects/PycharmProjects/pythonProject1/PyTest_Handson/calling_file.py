# from PyTest_Handson.inspect_stack import Hi
from PycharmProjects.PycharmProjects.pythonProject1.PyTest_Handson.inspect_stack import Hi


class Calling():

    def test_calling_function(self):
        hi = Hi()
        print(hi.raiseNotDefined())

janani = Calling()
janani.calling_function()


