import logging


def test_logging():
    loggerObj = logging.getLogger(__name__)
    filehandlerObj = logging.FileHandler("logfile.log")
    formatterObj = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
    loggerObj.addHandler(filehandlerObj)
    filehandlerObj.setFormatter(formatterObj)
    loggerObj.setLevel(logging.DEBUG)
    loggerObj.debug("I amd debug")
    loggerObj.info("I am info")
    loggerObj.warning("I am warning")
    loggerObj.error("I am error")
    loggerObj.critical("I am critical")