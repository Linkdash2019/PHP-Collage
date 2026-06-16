# Cameron McClellan 9/25/2024
# Lab 6

#Exercise 8-2: Favorite Book
def favorite_book(title):
    print("User's favorite book is", title + '.\n')

user_input = input('Please enter your favorite book. >>> ')
favorite_book(user_input)

#Exercise 8-3: T-Shirt
def make_shirt(size, message):
    print("Your shirt size is",size,"and the message printed on it is '"+message+"'!\n")

user_input = input('Enter the desired shirt size. >>> ')
user_input2 = input('Enter the text you would like displayed on the shirt. >>> ')
make_shirt(user_input, user_input2)
make_shirt(message='I got this shirt from "Legendary Shirts"!', size='XXl')

#Exercise 8-6: City Names
loop = 0

def city_country(city, country):
    global loop
    combined_input = f'"{user_input}, {user_input2}"'
    loop+=1
    return combined_input.title()

while loop < 3:
    user_input = input('Input a city. >>> ')
    user_input2 = input('Now input the country that city is from. >>> ')
    result = city_country(user_input, user_input2)
    print(result)
print()

#Exercise 8-9: Messages
def show_messages(pass_message):
    for show in pass_message:
        print(show)

messages = ['Hi.', 'Are you coming over today?', 'I need help with Math!', "When's the game show?"]
show_messages(messages)