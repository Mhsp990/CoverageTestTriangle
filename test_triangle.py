import pytest
from triangle import triangle_type

def test_notATriangle():
    assert triangle_type(0,10,20) == 'Not a triangle'
    assert triangle_type(10,0,20) == 'Not a triangle'
    assert triangle_type(10,20,0) == 'Not a triangle'
    assert triangle_type(0,0,0) == 'Not a triangle'
    assert triangle_type(5,13,5) == 'Not a triangle'
    assert triangle_type(3,3,6) == 'Not a triangle'
    assert triangle_type(3,10,5) == 'Not a triangle'

def test_equilateral():
    assert triangle_type(7,7,7) == 'Equilateral'

def test_isosceles():
    assert triangle_type(4,4,6) == 'Isosceles'
    assert triangle_type(6,4,4) == 'Isosceles'
    assert triangle_type(5,8,5) == 'Isosceles'

def test_scalene():
    assert triangle_type(7,9,12) == 'Scalene'

if __name__ == "__main__":
    pytest.main(['-v', '--cov=triangle', '--cov-fail-under=100'])