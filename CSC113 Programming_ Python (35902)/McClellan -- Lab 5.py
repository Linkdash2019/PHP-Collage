#

#Exersise 7-5 and 6
active = 0
age = -1
try:
    while active != 5:
        age = (input("Enter your age to find the price of a Movie Ticket. >>> ").strip())
        try:
            age = int(age)
        except:
            if age == "quit":
                break
            else:
                age = -1


        if age == -1:
            print('Invalid input')
            active = active-1
        elif age <= 3:
            print('Your movie ticket is $0')
        elif age <= 12:
            print('Your movie ticket is $10')
        elif age >= 13:
            print("Your movie ticket is $15")

        active += 1

except KeyboardInterrupt:
    print('\nKeyboard interrupt detected! Finishing early.\n')
if active == 5 or age == 'quit':
    print()

#Exersise 7-8
import time, random
done = 'False'
orders = ['Tuna', 'PB & Jam', 'Buttered Toast', 'PB & Honey', 'Meat Mix']
done_sandwich = []
while done == 'False':
    pop_sw = orders.pop()
    done_sandwich.insert(0, pop_sw)
    print("Order number", random.randrange(100, 999) , 'your', pop_sw, 'sandwich is done.')
    if not orders:
        done = 'True'
        print('All sandwiches done. We are now closing!')
    else:
        time.sleep(3)