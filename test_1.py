import pytest
import sys


@pytest.mark.smoke
def test_smoke():
    print('smoke test cases passed')

@pytest.mark.regression
def test_regression():
    print('regression test cases passed')

@pytest.mark.skip
def test_skip():
    print('skip test cases')


@pytest.mark.skipif(sys=sys.version_info<(3,8),reason='Test case is not yet ready')
def test_skipif():
    print('skipif test cases ')

@pytest.mark.parametrize('username,password',
                         [
                             ('Aishwarya','Aish123'),
                             ('as460','pwd')
                         ]
                         )
def test_parameterize(username,password):
    print('parameterize test cases passed')


@pytest.mark.xfail
def test_xfail():
    assert True
    print('xfail test cases')