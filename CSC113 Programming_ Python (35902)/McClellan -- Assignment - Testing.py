import pytest
from _McClellan__Assignment_Classes_EDITED import Rent_Car

@pytest.fixture()
def car_debugger():
    car_debug = Rent_Car('Bob', 'Ford', True, 1289)
    yield car_debug


def test_rent_car(car_debugger):
    car_debugger.get_car_price()

def test_return_car(car_debugger):
    car_debugger.return_car()

