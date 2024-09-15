import pytest


@pytest.mark.smoke
def test_smoke():
    print('smoke test cases passed')

@pytest.mark.regression
def test_regression():
    print('regression test cases passed')