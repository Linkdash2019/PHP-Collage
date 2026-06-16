# Cameron McClellan 8/29/2024
# Lab 2

#Exercise 3-1: Names
names = ['elijah', 'john', 'logan', 'maggie']
print('My friends are', names[0].title(), names[2].title(), names[-1].title(),'and', names[1].title() + '!! \n')

#Exercise 3-2: Greetings
phrase = ', you are an amazing friend!!'
print(names[0].title() + phrase)
print(names[3].title() + phrase, '(...and also my dog)')
print(names[1].title() + phrase)
print(names[-2].title() + phrase, '\n')

#Exersise 3-4: Guest List
dinner = ['elijah', 'aiden', 'evan']
invite = '! Dinner at 25:00 on Febuary 30, 9412!!'
print('Your invited', dinner[0].title() + invite)
print('Your invited', dinner[1].title() + invite)
print('Your invited', dinner[2].title() + invite, '\n')

#Exersise 3-5: Changing Guest List
Removed = [dinner[0]]
dinner[0] = 'james'
print(dinner)
print('Your invited', dinner[0].title() + invite)
print('Your invited', dinner[1].title() + invite)
print('Your invited', dinner[2].title() + invite)
print('Poor', Removed[0].title(), "texted me saying he couldn't come. \n")

#Exersise 3-6: More Guest
dinner.insert(0, 'logan')
dinner.insert(2, 'john')
dinner.append('dexter')
print('Got a bigger table!! Time too invite more people!!')
dinvar = 0
while dinvar < 6:
    print('Your invited', dinner[dinvar].title() + invite)
    dinvar= dinvar+1
print() #new line

#Exersise 3-8: Seeing the World
visit = ['japan', 'texas', 'florida', 'africa', 'greenland']
print(visit, '\n')

#Temp sort Alphabetically
print(sorted(visit), '\n')
print(visit, '\n')

#Temp sort Reverse-Alphabetically
print(sorted(visit, reverse=True), '\n')
print(visit, '\n')

#Reverse list
visit.reverse()
print(visit, '\n')
visit.reverse()
print(visit, '\n')

#Permanentaly sort Alphabetically
visit.sort()
print(visit, '\n')

#Permanentaly sort reverse Alphabetically
visit.sort(reverse=True)
print(visit, '\n')
