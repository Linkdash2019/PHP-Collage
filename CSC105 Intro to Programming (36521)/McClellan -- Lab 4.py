# Cameron McClellan 9/13/2024
# Lab 4

#Exercise 5-1: Conditional Tests
fav_color = 'Orange'
print ('fav_color is Orange')
print('Should be True!')
print(fav_color == 'Orange', '\n')

print('Should be False!')
print(fav_color == 'orange', '\n')

print('Should be True!')
print(fav_color.lower() == 'orange', '\n')

print('Should be True!')
print(fav_color.upper() == 'ORANGE', '\n')

print('Should be False!')
print(fav_color == 'oRANGE', '\n')

print('Should be True!')
print(fav_color.title() == 'Orange', '\n')

print('Should be False!')
print(fav_color == 'Red', '\n')

print('Should be False!')
print(fav_color == 'Red+Yellow', '\n')

print('Should be False!')
print(fav_color == 10, '\n')

print('Should be True!')
print(fav_color != 'Yellow', '\n')

#Exercise 5-2: More Conditional Tests
fav_food = "Banana"
print('fav_food is Banana')
print('Should be True!')
print(fav_food == 'Banana', '\n')

print('Should be True!')
print(fav_food != 'Onion', '\n')

print('Should be True!')
print(fav_food.lower() == 'banana', '\n')

print('Should be False!')
print(fav_food.lower() == 'Banana', '\n')

print('Should be True!')
print(10 > 3, '\n')

print('Should be False!')
print(10 > 99, '\n')

print('Should be True!')
print(10 >= 10, '\n')

print('Should be True!')
print(10 <= 10, '\n')

print('Should be True!')
print(10 > 100 or 10 > 1, '\n')

print('Should be True!')
print(10 > 9 and 99 < 100, '\n')

fav = ['Orange', 'Banana', 'Python', 'Video Games']
for item in fav:
    if item == 'Python':
        print('Favorite item "Python" found in list!')

if 'Ice Cream' not in fav: #This does not mean I don't like Ice Cream
    print('Ice Cream not found in list...\n')

#Exercise 5-3: Alien Colors #1
Alien_Color = 'green'
#No typo
if Alien_Color == 'green':
    print('Enemy Alien Defeated!')
    print('player got 5 EXP!\n')
else:
    pass
#Typo in IF (no output)
if Alien_Color == 'grenn':
    print('Enemy Alien Defeated')
    print('player got 5 EXP!\n')
else:
    pass

#Exercise 5-4: Alien Colors #2
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

#Exercise 5-8: Hello Admin

users = ['guest', 'admin', 'Cameron', 'Newton']
for user in users:
    if user == 'guest':
        print('Welcome to the computer Guest. If you need a tour press [ENTER] to close this window press [ESC]\n')
    elif user == 'admin':
        print('Welcome Admin! All systems appear operational. Should I run the debugger?\n')
    else:
        print('Welcome back', user + '! What would you like to do?\n')