import pytest


@pytest.mark.skip
@pytest.mark.regression
def test_multiple_case():
    test = 1+2
    assert test == 4, "Expected output is 4"

@pytest.mark.xfail
def test_demo_1():
    str1 = "janani"
    str2 = "jananidinesh"
    assert str1 in str2, "str1 is not in str2"

