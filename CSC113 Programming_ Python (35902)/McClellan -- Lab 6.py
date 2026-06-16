#Cameron McClellan 10/31/2024

#8-5. Cities
def describe_city(city_num):
    print(city_num['city'].title(), 'is in', city_num['country'].title())

city1 = {'city': 'tokyo', 'country': 'japan'}
describe_city(city1)
city2 = {'city': 'salt lake city', 'country': 'U.S.A'}
describe_city(city2)
city3 = {'city': 'mexico city', 'country': 'mexico'}
describe_city(city3)
print()

#8-7 and 8. Album and User Albums
import random

def make_album(name, title, number_song='Unknown'):
    num = {'artist_name': name, 'album_title': title, 'number_song': number_song}
    return num

artist_name = 'User'
album_title = 'favorites list'
album = make_album(artist_name, album_title, '0')

print('New album added:', album['album_title'].title(), 'created by', album['artist_name'].title(), '\nNumber of songs:', album['number_song'], '\n')

while True:
    album_title = input("Enter the name of album you would like to add. \n>>> ")
    if album_title.lower() == 'exit':
        break
    artist_name = input("Enter the artist of the chosen album. \n>>> ")

    #currently erases previous album
    question = random.randrange(1,3)
    if question == 1:
        album = make_album(artist_name, album_title)
    elif question == 2:
        album = make_album(artist_name, album_title, str(random.randrange(1, 300)))

    print('New album added:', album['album_title'].title(), 'created by', album['artist_name'].title(), '\nNumber of songs:', album['number_song'], '\n')

#8-9 and 10. messages and sending messages
def show_messages(message):
    for i in message:
        print(i)

def send_messages(message):
    loop = 0
    while loop !=3 :
        popped = messages.pop(0)
        print('Forwarding message:', popped)
        sent_messages.insert(-0,popped)
        loop += 1

messages = ['Did you order the pizza?', 'Do you want to hang out today?', 'Can you come over at 5:00 p.m?', '']
sent_messages = []
show_messages(messages)
send_messages(messages)

print(messages)
print(sent_messages)