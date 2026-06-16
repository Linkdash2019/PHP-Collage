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

class Rent_Bike(Rent_Car):
    def __init__(self, customer, rent_car, color, gears):
        self.color = color
        self.gears = gears
        super().__init__(customer, rent_car)

    def get_car_price(self):
        price = 30
        for var in range(self.gears):
            price += 5
        if self.color == 'red':
            price += 10
        elif self.color == 'blue':
            price += 4

        print('You want to borrow a', self.car, self.customer + '?')
        print(f'That will be ${price} an hour')
        print('Here is your bike', self.customer)


def main():
    global car
    while True:
        done = 'false'
        types_cars = ['volkswagen', 'toyota', 'ford', 'bmw', 'honda', 'hyundai', 'nissan', 'mazda', 'jeep', 'huston']
        car = input("What car do you want to borrow? >>> ").strip()

        print('Finding info on requested car:', car)
        time.sleep(2)

        #check success
        for list_car in types_cars:
            if car.lower() == list_car:

                # Jokes and giggles ##TotK Reference
                if car.lower() == 'huston':
                    print('Ah... The other-worldly hyruleian special.\nBe careful not to shake it or the Link branded sticky glue will come off!')
                    print(f'We have {random.randrange(1, 2)} available!!')
                    done = "true"
                #normal output
                else:
                    print('Found', car + '! We have', random.randrange(1, 5), 'available!!')
                    done = "true"



        #check fail
        if done == 'true':
            car_info()
            break
        elif done == 'false':
            print('Error: Unable to find', car, 'in database.')
        else:
            print('An error has occurred! Please try again or contact customer support if problem persists.')

def car_info():
    #Determine if is an Electric vehicle
    if (car.lower() == 'nissan') or (car.lower() == 'bmw') or (car.lower() == 'huston'):
        electric = True
    else:
        electric = False

    milage = random.randrange(500, 70000)
    chosen_car = Rent_Car(name, car.lower(), electric, milage)
    chosen_car.get_car_price()
    input('Press [ENTER] to return the car')
    chosen_car.return_car()

car = 'N/A'
name = input("Hello sir, What is your name? >>> ")
main()
print('----------------------------------------')
car_debug = Rent_Car('Bob', 'Ford', True, 1289)
car_debug.get_car_price()
car_debug.return_car()
print('----------------------------------------')
bike1 = Rent_Bike('Wolly', "Kid's bike", "blue", 5)
bike1.get_car_price()
bike1.return_car()
print('----------------------------------------')
bike2 = Rent_Bike('Bill', "Fat Wheels bike", "red", 5)
bike2.get_car_price()
bike2.return_car()

