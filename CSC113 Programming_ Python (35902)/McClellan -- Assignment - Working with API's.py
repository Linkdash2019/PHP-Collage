import requests

cache = dict()

def get_page_from_server(url):
    print("Fetching data from server...")
    response = requests.get(url)
    return response.json()

def get_page(url):
    print("Getting data...")
    if url not in cache:
        cache[url] = get_page_from_server(url)

    return cache[url]

def screen_refresh():
    print('---------------------------------------------')
    print("\033[H\033[J", end="")

def do_choice():
    if command == 1:
        num_search()
    elif command == 8:
        exit()
    elif command == 9:
        user_help()
    else:
        print("That's not a valid command enter '9' for help.")

def num_search():
    valid = False
    while not valid:
        try:
            valid = True
            command2 = int(input('Enter a Pokedex number. >>> '))
        except:
            valid = False
            print("That's not a number!")

    page = get_page(f'https://pokeapi.co/api/v2/pokemon/{command2}/')
    screen_refresh()
    pokedex(page)

def pokedex(pokemon):
    try:
        print(f"Chosen Pokemon: {(pokemon['forms'][0]['name'].title())}")
    except:
        print('Pokemon not found.')
    try:
        type2 = (pokemon['types'][1]['type']['name'])
    except:
        type2 = 'none'
    print(f"Types: {(pokemon['types'][0]['type']['name']).title()}, {type2.title()}")
    print(f"Weight: {pokemon['weight']}")

    input('Press [ENTER] to continue')
    screen_refresh()

def user_help():
    print('HELP:\n1 - Search Pokemon with Pokedex number\n8 - Clear cache and exit\n9 - Print this help message\n2-7 - Reserved for future updates')

user_help()
while True:
    try:
        command = int(input("What would you like to do? >>> "))
        screen_refresh()
    except:
        print("That's not a valid command enter '9' for help.")
    else:
        do_choice()