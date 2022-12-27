import pytest


def inc(x):
    return x * 2


def test_pos():
    assert inc(3) == 6  # ok


def test_neg():
    assert inc(-2) == -4  # ok


def test_pos():
    assert inc(3) == 5  # will be fail
