#Cameron McClellan 10/21/2014
#Lab 2

#3-2: Greetings
names = ['elijah', 'john', 'logan', 'maggie']
print('My friends are', names[0].title(), names[2].title(), names[-1].title(),'and', names[1].title() + '!! \n')

phrase = ', you are an amazing friend!!'
print(names[0].title() + phrase)
print(names[3].title() + phrase, '(...and also my dog)')
print(names[1].title() + phrase)
print(names[-2].title() + phrase, '\n')

#3-4. Guest List
dinner = ['elijah', 'aiden', 'evan']
invite = '! Dinner at 25:00 on Febuary 30, 9412!!'
print('Your invited', dinner[0].title() + invite)
print('Your invited', dinner[1].title() + invite)
print('Your invited', dinner[2].title() + invite, '\n')

#3-5. Changing Guest List
Removed = [dinner[0]]
dinner[0] = 'james'
print('Your invited', dinner[0].title() + invite)
print('Your invited', dinner[1].title() + invite)
print('Your invited', dinner[2].title() + invite)
print('Poor', Removed[0].title(), "texted me saying he couldn't come. \n")

#3-6. More Guests
dinner.insert(0, 'logan')
dinner.insert(2, 'john')
dinner.append('dexter')
print('Got a bigger table!! Time too invite more people!!')
dinvar = 0
while dinvar < 6:
    print('Your invited', dinner[dinvar].title() + invite)
    dinvar= dinvar+1
print() #new line

#3-7. Shrinking Guest List
popped = dinner.pop()
print('Sorry', popped.title(), "the table didn't come quick enough")
popped = dinner.pop(3)
print('Sorry', popped.title(), "the table didn't come quick enough")
popped = dinner.pop(-2)
print('Sorry', popped.title(), "the table didn't come quick enough")
popped = dinner.pop(0)
print('Sorry', popped.title(), "the table didn't come quick enough\n")


for name in dinner:
    print("Congrats", name.title() + "! There is still space at the table for you to come!")

del dinner[0]
del dinner[0]
print(dinner,'\n')

#4-2. Animals
animals = ['cow', 'pig', 'chicken']
for animal in animals:
    print(animal.title() + "'s exist in the blocky world of Minecraft.")

print('All these animals exist in Minecraft!!\n')

#4-3. Counting to Twenty
for value in range(1, 21):
    print(value)
print() #New line

#4-7. Threes
three = []
for value_new_again in range(3, 31, 3):
    three.append(value_new_again)
for number in three:
    print(number)
print() #New Line

#4-10. Slices
print('The list used in this exercise is "three" created in 4-7')
print('The first 3 items in the list are:', three[:3])
print('The items in the middle of the list are:', three[4:-4])
print('The last 3 items in the list are:', three[-3:])