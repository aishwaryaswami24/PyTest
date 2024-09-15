import pytest


@pytest.mark.smoke
def test_script1():
    print('smoke test cases passed')

@pytest.mark.regression
def test_login():
    print('regression test cases passed')