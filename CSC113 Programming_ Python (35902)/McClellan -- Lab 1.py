#Cameron McClellan
#10/8/2024
#Lab 1


#Exersise 2-2: Simple Messages
vmessage2 = "Message one!"
print(vmessage2)
vmessage2 = "Message two!!"
print(vmessage2,'\n')

#Exersise 2-4: Name Cases
fname = "Cameron"
mname = "Scott"
lname = "McClellan"
fullname = f"{fname} {mname} {lname}"
print(fullname.title())
print(fullname.upper())
print(fullname.lower(),'\n')

#Exercise 2-6: Famous Quote 2
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(famous_person,'has said,', message, '\n')

#Exercise 2-7: Stripping Name
name = '\t             Cameron M          \n'
print(name)
print(name.rstrip().lstrip(), '\n')

#Exercise 2-8: File Extensions
filename = 'pythonnotes.txt'
print(filename.removesuffix('.txt'),'\n')

#Exersise 2-9: Number 8
print(2+6)
print(18-10)
print(2*2*2)
print(64/8)

#Exersise: Canvas
print('My name is Cameron M')
print('I live in Dewey, AZ')
print('')
print('I use my personal Computer to do classwork')
print('My hobbies include Looking through source code, playing video games, and compiling software. (Yes, I like programming that much)')
print('Shhh, but I found out how to run Minecraft on the YC computers and now trying to figure out how I can use the mcpi python library with it')