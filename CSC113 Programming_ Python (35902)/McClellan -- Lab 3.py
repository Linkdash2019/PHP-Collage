#Exercise 5-4: Alien Colors #2
Alien_Color = 'green'

if Alien_Color == 'green':
    print('Enemy Alien Defeated!')
    print('Player got 5 EXP!\n')
else:
    print('Strong Enemy Alien Defeated!')
    print('Player got 10 EXP!\n')

Alien_Color = 'yellow'
if Alien_Color == 'green':
    print('Enemy Alien Defeated!')
    print('Player got 5 EXP!\n')
else:
    print('Strong Enemy Alien Defeated!')
    print('Player got 10 EXP!\n')

#Exercise 5-5: Alien Colors #3
Aliens = ['green', 'yellow', 'red']
for Alien_Color in Aliens:

    if Alien_Color == 'green':
        print('Enemy Alien Defeated!')
        print('Player got 5 EXP!\n')
    elif Alien_Color == 'yellow':
        print('Strong Enemy Alien Defeated!')
        print('Player got 10 EXP!\n')
    elif Alien_Color == 'red':
        print('Boss Alien Defeated!')
        print('Player got 15 EXP!\n')

#Exersice 5-6: Stages of Life
age = int(input('How old are you?\n>>> '))
if age < 2:
    print('You are a baby')
elif age >= 2:
    print('You are a toddler')
elif age >= 4:
    print('You are a kid')
elif age >= 13:
    print('You are a teenager')
elif age >= 20:
    print('You are a adult')
elif age >= 65:
    print('You are a elder')
#Exercise 5-8: Hello Admin
users = ['guest', 'admin', 'Cameron', 'Newton']
for user in users:
    if user == 'guest':
        print('Welcome to the computer Guest. If you need a tour press [ENTER] to close this window press [ESC]\n')
    elif user == 'admin':
        print('Welcome Admin! All systems appear operational. Should I run the debugger?\n')
    else:
        print('Welcome back', user + '! What would you like to do?\n')

#Exercise 5-9: No Users
users = []
if users:
    for user in users:
        if user == 'guest':
            print('Welcome to the computer Guest. If you need a tour press [ENTER] to close this window press [ESC]\n')
        elif user == 'admin':
            print('Welcome Admin! All systems appear operational. Should I run the debugger?\n')
        else:
            print('Welcome back', user + '! What would you like to do?\n')
else:
    print("No user's found. Proceeding to account creation...\n")
#Exercise 5-10: Checking Usernames
cusers = ['Cameron', 'Newton', 'John', 'Beth', 'Will']
nusers = ['John', 'Cameron', 'Linkdash', 'Gwen', 'Grazzy']

for name in nusers:
    if name in cusers:
        print(name+'#2 That username already is in use.')
    else:
        print(name, 'That is a valid username. Account successfully created!')
    print()

#Exercise 5-11: Ordinal Numbers
number = [1,2,3,4,5,6,7,8,9]
for item in number:
    if item == 1:
        print("{}st".format(item))
    elif item == 2:
        print("{}nd".format(item))
    elif item == 3:
        print("{}rd".format(item))
    elif item >= 4:
        print("{}th".format(item))