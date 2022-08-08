import pytest


# @pytest.mark.usefixtures
from PycharmProjects.PycharmProjects.pythonProject1.PyTest_Handson.inspect_stack import Hi


class Test_headless:
    def test_headless(self):
        hello = Hi()
        print(hello.raiseNotDefined())
