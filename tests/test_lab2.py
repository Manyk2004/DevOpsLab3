import pytest

from src.lab2_calc import quad, add_fn, sub_fn, mult_fn, div_fn

def test_quad():
    assert test_quad(1,0,-1) == -1, 1
    assert test_quad(0,1,1) == -1, -1
    assert test_quad(1,2,1) == -1, -1
    assert test_quad(1,2,0) == -2, 0

def test_add_fn():
    assert add_fn(1,1) == 2
    assert add_fn(2,2) == 4
    assert add_fn(4,4) == 8
    assert add_fn(8,8) == 16

def test_sub_fn():
    assert sub_fn(1,0) == 1
    assert sub_fn(2,1) == 1
    assert sub_fn(4,2) == 2
    assert sub_fn(8,3) == 5

def test_add_fn():
    assert mult_fn(1,1) == 1
    assert mult_fn(2,2) == 4
    assert mult_fn(4,4) == 16
    assert mult_fn(8,8) == 64

def test_add_fn():
    assert div_fn(1,1) == 1
    assert div_fn(2,2) == 1
    assert div_fn(4,3) == 4/3
    assert div_fn(8,4) == 2
