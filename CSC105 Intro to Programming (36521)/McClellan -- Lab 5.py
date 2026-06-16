# Cameron McClellan 9/20/2024
# Lab 5

import time
import random

#Exercise 7-1: Rental Car
done = 'false'
types_cars = ['volkswagen', 'toyota', 'ford', 'bwm', 'honda', 'hyundai', 'nissan', 'mazda', 'jeep']
car = input("What car do you want to borrow? >>> ").strip()

print('Finding info on requested car:', car)
time.sleep(2)

#check success
for list_car in types_cars:
    if car.lower() == list_car:
        print('Found', car + '! We have', random.randrange(1, 5), 'available!!')
        done = "true"
#check fail
if done == 'true':
    pass
elif done == 'false':
    print('Error: Unable to find', car, 'in database.')
else:
    print('An error has occurred! Please try again or contact customer support if problem persists')

#new line
print()

#Exercise 7-2: Restaurant Seating
answered = 'false'

print('Welcome to Bills Taco Place!')
while answered == 'false':
    try:
        people = int(input("How many people are in your group? >>> ").strip())
    except:
        print("Error! please make sure to input numbers like '1, 2, 3, ect.'\n")
    else: answered = 'true'
if people == 0:
    print('Come on! Stop messing around!')
elif people <= 8:
    print('Alright, please follow me to your table.')
elif people <= 16:
    print('Please wait for an available table.')
elif people >= 17:
    print("I'm afraid we don't have a table that size!")

#new line
print()

#Exercise 7-4: Pizza Toppings
ask = 'nothing'
toppings = []
print("You are ordering from Billy's Melting Pizza. \nPlease insert what topping you would like. \nWhen your done type 'done'!\n")
while ask != 'Done':
    ask = input('What topping would you like on you Pizza? >>> ').strip().title()
    if ask !='Done':
        toppings.append(ask)
        print('Added', ask, 'to your Pizza successfully! \nYou have the following ingredients on you Pizza: \n', toppings, '\n')
    else:
        print("Thank you for ordering at Billy's Melting Pizza\n")


#Exercise 7-5: Movie Tickets
age = 'start'

while age != 'quit':
    age = (input("Enter your age to find the price of a Movie Ticket. >>> ").strip())
    try:
        age = int(age)
    except:
        break

    if age <=3:
        print('Your movie ticket is $0')
    elif age <= 12:
        print('Your movie ticket is $10')
    elif age >= 13:
            print("Your movie ticket is $15")