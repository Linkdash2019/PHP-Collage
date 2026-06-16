#Cameron McClellan 11/1/24
# Lab 11
import pytest


# Exercise 11-1 and 2
def place(city, country, population='Unknown'):
    combined = (city + ', ' + country + ' -- population = ' + population)
    return combined

# Exercise 11-3: Employee
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, salary_raise = 5000):
        self.salary_raise = salary_raise
        self.salary += salary_raise
        return self.salary
