import mathe
import pytest

@pytest.mark.parametrize('num1, num2, result',
                        [(7, 3, 10),
                        ('hello', ' world', 'hello world'),
                        (10.5, 11.5, 22),])


def test_add(num1, num2, result):
    assert mathe.add(num1, num2) == result