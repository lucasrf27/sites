import pytest

def add_test():
    assert pytest.add(2,5) == 8
    assert pytest.add(2) == 4

