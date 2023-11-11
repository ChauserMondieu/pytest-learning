import pytest


def setup_module():
    print("\n setup_module: whole python script will only operate once")


def teardown_module():
    print("teardown_module: thw whole python script will ony operate once")


def setup_function():
    print("setup_function: operate at the start of each non-class test instance ")


def teardown_function():
    print("teardown_function: operate at the end of each non-class test instance ")


def test_one():
    print("operating test module --- test_one")


def test_two():
    print("operating test_module --- test two")

