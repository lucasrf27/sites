from phonebook import PhoneBook, add
import pytest

t1 = PhoneBook('bob', 1234)


def test_add():
    assert t1 == {'bob' : 1234}


def test_add2():
    assert add(5, 2) == 7