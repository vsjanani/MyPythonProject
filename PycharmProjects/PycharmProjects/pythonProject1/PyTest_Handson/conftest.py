import inspect

import pytest


@pytest.fixture(scope="class")
def test_browser_close_open():
    print("browser opened")
    yield
    print("browser closed")


@pytest.fixture(scope="class")
def test_data_setup(request):
    login_details = ("janani", "dinesh", "darshini", "sanjeevkrish")
    print('datasetup check')
    # return request.param
    request.cls.login = login_details


@pytest.fixture(params=("chrome", "firefox"))
def test_browsers(request):
    return request.param


@pytest.fixture(scope="class")
def test_log_caller_fixture():
    print("fixture browser opened")
    yield
    print("fixture browser closed")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


