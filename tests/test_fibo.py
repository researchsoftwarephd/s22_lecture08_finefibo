import pytest
from finefibo.fibo import fibo_number

@pytest.mark.parametrize('n, expected', [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (12, 144)])
def test_fibo_number_values(n, expected):
    assert fibo_number(n) == expected

def test_fibo_number_errors():
    with pytest.raises(ValueError):
        fibo_number(-1)
    with pytest.raises(TypeError):
        fibo_number(-1.4)
    with pytest.raises(TypeError):
        fibo_number('hello world')
    with pytest.raises(TypeError):
        fibo_number((1, 2, 3, 4))