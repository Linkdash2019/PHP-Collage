#Cameron McClellan 11/6/2024
#This should be called lab 7 not 9!

#Exercise 9-6: Ice Cream Stand
#Includes 9-1: Restaurant
#9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self. cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Name:', self.restaurant_name)
        print('Food:', self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, 'is currently open!')

restaurant = Restaurant("Aiden's Hearty Salads", 'Salad')
print('Received info:', restaurant.restaurant_name,'|', restaurant.cuisine_type)

print('----------------------------------------------------')

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavor):
        self.flavor = flavor
        super().__init__(restaurant_name, cuisine_type)

    def describe_restaurant(self):
        print('Name:', self.restaurant_name)
        print('Food:', self.cuisine_type)
        print('Flavors:', ', '.join(self.flavor))

flavors = IceCreamStand('Icy Sweet Stand', 'Ice Cream', ['Vanilla', 'Chocolate', 'Mint Choco-Chip'])
flavors.describe_restaurant()

#Exercise 9-7: Admin
#Includes 9-3: Users
#9-3
class User:
    def __init__(self, first_name, last_name, username, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.age = age

    def describe_user(self):
            hidden_pass = []
            for var in self.password:
                hidden_pass.append('*')
            new_hidden_pass = ''.join(hidden_pass)

            print('User:', self.username)
            print('Password:', new_hidden_pass)
            print('Name:', self.first_name, self.last_name)
            print('Age:', self.age)

    def greet_user(self):
        print('Welcome back',self.first_name + '. There no updates to run as of now.')

user1 = User('Cameron', 'McClellan', 'Linkdash','NotAPassword1234', '16')
user2 = User('William', 'Fordna', 'tiny_Mincrafter','password', '8')
user3 = User('Bob', 'Bilbo', 'Bagens','Gandolf', '47')
user4 = User('Scroodge', 'Mcduck', 'Adventure_Ducky','ILoveGold999', '98')

print('----------------------------------------------------')
user1.describe_user()
print('----------------------------------------------------')
user2.describe_user()
print('----------------------------------------------------')
user3.describe_user()
print('----------------------------------------------------')
user4.describe_user()

print('----------------------------------------------------')
user1.greet_user()
print('----------------------------------------------------')
user2.greet_user()
print('----------------------------------------------------')
user3.greet_user()
print('----------------------------------------------------')
user4.greet_user()
print('----------------------------------------------------')

#9-7
class Admin(User):
    def __init__(self, first_name, last_name, username, password, age , privileges):
        self.privileges = privileges
        super().__init__(first_name, last_name, username, password, age)

    def show_privileges(self):
        print(self.username,'has the following permissions:\n' + ', '.join(self.privileges))

    def new_show_privileges(self):
        your_privileges = Privileges(self.privileges)
        your_privileges.show_privileges()


admin = Admin('Root', 'N/A', 'Admin', 'tooR', 'N/A', ['Read Files', 'Write Files', 'Execute Files', 'Manage Users'])
admin.show_privileges()

print('----------------------------------------------------')


#Exercise 9-8: Privileges
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('You have the following permissions:\n' + ', '.join(self.privileges))

admin2 = Admin('Root', 'N/A', 'Admin', 'tooR', 'N/A', ['Read Files', 'Write Files', 'Execute Files', 'Manage Users'])
admin2.new_show_privileges()

print('----------------------------------------------------')

#Exercise 9-9: Battery Upgrade

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        print(f"Upgrading your {self.battery_size}-kWh battery.")
        self.battery_size = 65

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()