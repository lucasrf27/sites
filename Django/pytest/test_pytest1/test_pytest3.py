from data import Data
import pytest


#db=None

#def setup_module(module):
#    print('-----------SETUP----------------')
#    global db
#    db = Data()
#    db.connect('data.json')


#def teardown_module(module):
#    print('-----------teardown----------------')
#    db.close()

@pytest.fixture(scope='module')
def db():
    print('-----------SETUP----------------')
    global db
    db = Data()
    db.connect('data.json')
    yield db
    print('-----------teardown----------------')
    db.close()




def test_scott(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
