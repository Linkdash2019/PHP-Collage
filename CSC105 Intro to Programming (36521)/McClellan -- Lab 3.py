# Cameron McClellan 8/5/2024 -- 8/6/2024
# Lab 3

#Exercise 4-1: Pizza
fav_pizza = ['pepperoni', 'mexican', 'hawaiian']
for pizza in fav_pizza:
    print('I love', pizza.title(), 'Pizza!')

print('Pizza is verrry delicious!!!\n')

#Exercise 4-2: Animals
animals = ['cow', 'pig', 'chicken']
for animal in animals:
    print(animal.title() + "'s exist in the blocky world of Minecraft.")

print('All these animals exist in Minecraft!!\n')

#Exercise 4-3: Count to 20
for value in range(1, 21):
    print(value)
print() #New line

#Exercise 4-6: Odd Numbers
for value_new in range(1, 21, 2):
    print(value_new)
print() #New line

# Exercise 4-7: Threes
three = []
for value_new_again in range(3, 31, 3):
    three.append(value_new_again)
for number in three:
    print(number)
print() #New Line

# Exercise 4-10: Slices
print('The list used in this exercise is "three" created in 4-7')
print('The first 3 items in the list are:', three[:3])
print('The items in the middle of the list are:', three[4:-4])
print('The last 3 items in the list are:', three[-3:])