import pytest


@pytest.mark.usefixtures("test_browser_close_open")
class TestVerification:
    def test_login(self):
        print("login verified successfully")

    def test_login_details(self, test_data_setup):
        # print(test_data_setup)
        print(self.login[0])

    def test_cross_browsers(self, test_browsers):
        print(test_browsers)




