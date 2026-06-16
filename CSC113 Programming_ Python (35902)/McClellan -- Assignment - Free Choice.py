############
#          #
#        /----\
#       | ' ' |
#       \____/
#        | |
#      /[---]\
#     / [   ] \
#   /  [___]  \
#      /  \
#     /    \
#    /      \
#

import time

lives = 6
word = 'hangman'
lettercnt = 0
right = []
wrong = []
obscure = []
print('Welcome to this Python adaptation of Hangman! Your goal is to guess the secret word in 6 tries. \nYou may guess the WHOLE word or you may guess a single LETTER in the word to slowly construct it')

print("The game starts NOW!\n")

for item in word:
    lettercnt +=1
    obscure.append('_')
print('There are', lettercnt, 'letters in this word')

while lives !=0:
    if '_' in obscure:
        pass
    else:
        break

    print("Guesses left:", lives)
    print('Word', ' '.join(obscure))
    print('Incorrect guesses', ', '.join(wrong))
    guess = input("\nInput a WORD or LETTER for your guess\n>>> ").lower().strip()

    #Determine if guess is word or letter
    letters = 0
    for item in guess:
        letters += 1

    #If no input
    if letters == 0:
        print("\nNo input received")

    #Determine if is Alphabetical
    if not guess.isalpha():
        print("Foreign character detected!\nPlease only enter LETTERS")
        if guess == '/':
            guess = -1
        else:
            guess = ''



    #If is letter
    try:
        if letters == 1:
            if (guess in right) or (guess in wrong):
                print('Error letter already guessed')

            elif guess in word:
                print(guess, "is correct!")
                right.append(guess)

                num_check = 0
                test_word = word

                while word.count(guess) != num_check:
                    num_check += 1
                    obscure[test_word.find(guess)] = guess
                    test_word = test_word.replace(guess, '-', 1)
            else:
                print(guess, "is incorrect.")
                wrong.append(guess)
                lives -= 1
    except:
        pass

    #If is word
    try:
        if letters > 1:
            if guess == word:
                print(guess, "is correct!")
                break
            if guess == '':
                pass
            else:
                print(guess, "is incorrect.")
                lives -= 1
    except:
        pass

    #Refresh the terminal beautifully for most systems
    print("Waiting...")
    time.sleep(3)
    print('---------------------------------------------')
    print("\033[H\033[J", end="")

#Win/Lose logic
if lives == 0:
    print("You lost...")
else:
    print("You WIN!")

print('The word is', word)

exit = input('Press [ENTER] to exit')
