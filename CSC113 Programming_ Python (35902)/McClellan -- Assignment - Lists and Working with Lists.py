import random

def get_nouns():
    noun1 = input("\nWhat is the first noun?\n>>> ")
    noun2 = input("What is the second noun?\n>>> ")
    noun3 = input("What is the third noun?\n>>> ")
    global nouns
    nouns = [noun1, noun2, noun3]

def get_verbs():
    verb1 = input("\nWhat is the first verb?\n>>> ")
    verb2 = input("What is the second verb?\n>>> ")
    verb3 = input("What is the third verb?\n>>> ")
    global verbs
    verbs = [verb1, verb2, verb3]

def get_adjectives():
    adjective1 = input("\nWhat is the first adjective?\n>>> ")
    adjective2 = input("What is the second adjective?\n>>> ")
    adjective3 = input("What is the third adjective?\n>>> ")
    global adjectives
    adjectives = [adjective1, adjective2, adjective3]

def get_articles():
    article1 = input("\nWhat is the first article?\n>>> ")
    article2 = input("What is the second article?\n>>> ")
    global articles
    articles = [article1, article2]

#Begin program
choice = input("Would you like to use the default words? \n(y)es or (n)o\n>>> ")

if (choice.lower() == 'y') or (choice.lower() == 'yes'):
    nouns = ['guy', 'cow', 'dog']
    verbs = ['ran', 'jumped', 'fell']
    adjectives = ['red', 'stubborn', 'strange']
    articles = ['the', 'that']

elif (choice.lower() == 'n') or (choice.lower() == 'no'):
    get_nouns()
    get_verbs()
    get_articles()
    get_adjectives()

else:
    print("Error!\nInvalid option chosen!")
    exit(1)
#Caculate phrase
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
article = random.choice(articles)

print('\n'+article.title(), adjective, noun, verb+'.')