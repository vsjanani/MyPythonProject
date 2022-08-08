import inspect
import logging

# import pytest


class TestLogger:
    def test_logger(self):
        loggerName = inspect.stack()[1][3]
        logObj = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logger.log")
        formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        logObj.addHandler(fileHandler)
        fileHandler.setFormatter(formatter)
        logObj.setLevel(logging.ERROR)
        return logObj

