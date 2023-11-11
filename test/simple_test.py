import pytest


def test_one():
    assert 1 == 1
    print("this is one test function ...")


if __name__ == '__main__':
    pytest.main("-s", "simple_test.py")
