import time
import random

class Rent_Car:
    def __init__(self, customer, rent_car, is_electric=False, driven_miles='N/A'):
        self.customer = customer
        self.car = rent_car
        self.is_electric = is_electric
        self.driven_miles = driven_miles

    def get_car_price(self):
        price = 5000
        if self.is_electric:
            price += 2000

        price_mile_calc = 0
        for var in range(self.driven_miles):
            price_mile_calc += 1
            if price_mile_calc == 100:
                price_mile_calc = 0
                price -= 1

        if self.car == 'huston':
            price += 15000
        print('You want to borrow a', self.car, self.customer + '?')
        print('This car has driven', self.driven_miles, 'miles.')
        print(f'That will be ${price} a day')
        print('Here is your car', self.customer)

    def return_car(self):
        if self.driven_miles == 'N/A':
            pass
        else:
            print('It looks like you drove about 1000 miles for 1 day')
            self.driven_miles += 1000
            print('New milage is', self.driven_miles)
        print('The', self.car, 'has been retrieved', self.customer + '. Thank you for using our services!')



