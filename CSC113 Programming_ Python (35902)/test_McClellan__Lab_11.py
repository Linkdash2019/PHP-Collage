# Cameron McClellan 11/1/24
# Lab 11 TEST
import pytest

# Exercise 11-1 and 2
from McClellan__Lab_11 import place

def test_place():
    print(place('Phoenix', 'Arizona'))

def test_place_population():
    print(place('Phoenix', 'Arizona', "lol I still don't know!"))

# Exercise 11-3: Employee
from McClellan__Lab_11 import Employee

@pytest.fixture()
def employee():
    employee = Employee("FName", "LName", 50)
    return employee

def test_give_default_raise(employee):
    print(employee.give_raise())

def test_give_custom_raise(employee):
    print(employee.give_raise(3))

