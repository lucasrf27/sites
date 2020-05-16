import mathe
import pytest
import sys

@pytest.mark.skipif (sys.version_info < (3, 3), reason='i want')
def test_add():
    assert mathe.add(2) == 4
    assert mathe.add(2,5) == 7
    assert mathe.add(2) == 4
    print (mathe.add(5,5), 'foda-se')


def test_prod():
    assert mathe.prod(2) == 4
    assert mathe.prod(2,5) == 10
    assert mathe.prod(2) == 4


def test_add_strings():
    result = mathe.add('hello', ' world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'hello' in result
