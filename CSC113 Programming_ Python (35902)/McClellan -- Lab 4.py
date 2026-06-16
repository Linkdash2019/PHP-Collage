#Exersise 6-3: Glossary
glossary = {
    'print': 'Sends given words or integers to the terminal as output.',
    'list': 'Stores many strings or integers as callable data.',
    'dictionary': 'Stores data similar too lists but you can store infinite sub-data about items in the dictionary.',
    'if/elif/else/finally': '4 statements executed in the order shown. if/elif run if the condition given is true.\n else runs if none of the if/elif statements are true. finally runs last regardless of the rest of the statements.',
    'variables': 'Bits of data reserved for storing what you need such as strings or integers.',
}

print('Print:\n', glossary['print'], '\n')
print('List:\n', glossary['list'], '\n')
print('Dictionary:\n', glossary['dictionary'], '\n')
print('if/elif/else/finally:\n', glossary['if/elif/else/finally'], '\n')
print('Variables:\n', glossary['variables'])
print('----------------------------------------------------------------------------------')

#Exersise 6-4: Glossary 2
glossary['comment'] = 'A line of code the interpreter ignores. Used for clarity.'
glossary['while'] = 'Start looping until the given condition is no longer true.'
glossary['input'] = 'Allows user input from keyboard. Defaults to string but can be integer.'
glossary['import'] = 'Allows importing a module that is installed such as random or tkinter'
glossary['exit()'] = 'Terminates the program with the exit code defined. if not exit code is defined exit with code 0'

for item in glossary:
    print(item.title() + ':\n', glossary[item], '\n')
print('----------------------------------------------------------------------------------')

#Exersise 6-5: Rivers
rivers = {
    'Amazon': 'Brazil',
    'Mississippi': '10 different states in North America',
    'Orinoco': 'Venezuela',
}

for item in rivers:
    print('The', item.title(), 'river runs through', rivers[item], '\n')

#Exersise 6-8: Pets
maggie = {"name": "maggie", "type": "dog", "owner": "cameron"}
knight = {"name": "knight", "type": "dog", "owner": "elijah"}
blue = {"name": "blue", "type": "bird", "owner": "evan"}

pets = [maggie, knight, blue]

for pet in pets:
    print(f'Name: {pet['name'].title()}')
    print(f'Type: {pet['type'].title()}')
    print(f'Owner: {pet['owner'].title()}')
    print('---------------------------')

#Exersise 6-11: Cities
cities = {
    'Phoenix': {
        'country': 'USA, Arizona',
        'population': '1,662,607',
        'fact': "It's very HOT",
    },

    'Salt Lake': {
        'country': 'USA, Utah',
        'population': '212,570',
        'fact': "There is this thing called snow over there"
    },

    'Mexico City': {
        'country': 'Mexico',
        'population': '22,505,300',
        'fact': 'One of the worlds LARGEST cities'
    }
}

for city, info in cities.items():
    print(city)
    print(info['country'])
    print(info['population'])
    print(info['fact'], '\n')