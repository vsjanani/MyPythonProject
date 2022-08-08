import pytest


@pytest.mark.usefixtures("test_log_caller_fixture")
class TestCheck:

    def test_demo(self, test_data_setup):
        # print(test_data_setup())
        print(self.login[0])
        print("check test_ validation")

    def test_demo1(self, chumma):
        print("Sarvam Krishnarpanam")
        # print(test_data_setup()]
        # print(self.login[0])
        print(chumma["name"])

    def test_mytestCase(self):
        print("Vanakkam")

    @pytest.fixture(params = [{"name" : "dinesh", "age" : "26"}])
    def chumma(self, request):
        login_details = ("janani", "dinesh", "darshini", "sanjeevkrish")
        # print('datasetup check')
        return request.param
        # request.cls.login = login_details
