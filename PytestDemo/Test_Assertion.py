import pytest
def test_sample_one():
    print("Hai")
def test_sample1():
    a=10
    b=10
    assert a!=b
def test_sample2():
    a=5
    b=10
    assert a==b
def test_sample3():
    a = "arun"
    b = "aruns"
    assert a.__eq__(b)