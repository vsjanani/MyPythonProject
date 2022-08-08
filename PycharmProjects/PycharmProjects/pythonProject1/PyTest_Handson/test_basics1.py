# import pytest
#
# @pytest.fixture()
# def test_case0():
#     print("browser invocation")
#     yield
#     print("close browser")
#
# @pytest.mark.usefixtures("test_case0")
# class Dummy:
#
#     def test_case1(self):
#         print('regular test case1')
#
#     def test_case2(self):
#         print("regular test case2")
#
#     def test_case3(self):
#         print("regular test case3")
#
#
# myObj = Dummy()
# myObj.test_case1()
# myObj.test_case2()
# myObj.test_case3()
#

import pytest


@pytest.mark.usefixtures("test_data_setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")

#
# def callfixture(setup):
#     x = TestExample()
#     x.test_fixtureDemo1()

