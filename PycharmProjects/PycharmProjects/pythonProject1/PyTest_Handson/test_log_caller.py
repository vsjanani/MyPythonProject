import pytest

from PyTest_Handson.test_logger import TestLogger


@pytest.mark.usefixtures("test_log_caller_fixture")
class TestLogCaller(TestLogger):
    def test_log_caller(self):
        log = self.test_logger()
        log.debug("Sarvam Krishnarpanam")
        log.info("i am info")
        log.critical("I am critical")
        log.warning("I am warning")
        log.error("i am error")


