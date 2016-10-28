import random, string, time

LIFE = 5

def pick_cap():
    '''Randomly picks a capital from a txt file'''

    List = open("eucaps.txt").readlines()
    capital = random.choice(List).upper()[0:-1] #indeksowanie FTW!
    return (capital)



def display(capital,guessed):
    '''Displays current stage of capital that is being guessed'''

    for letter in capital:
        if letter in guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')


def check_win(guessed,capital):
    '''Checks if user has won by guessing all the single letters.
        Returns True if that's the case, False otherwise'''

    for letter in capital:
        if letter not in guessed:
            return False
    return True

def decision():
    '''Asks if user wants to enter a letter or a word as the guess.
        Checks if the guess is legal and returns it'''

    legal = string.ascii_uppercase + ' '

    while True:
        decision = input("Would you like to guess a letter or the whole word? (W/L): ").upper()

        if decision == "W":
            while True:
                word = input("Hit me with your word: ").upper()
                if len(word) < 2:
                    print("That's too short for a word!")
                else:
                    for e in word:
                        if e not in legal:
                            print('What kind of school did you go to?!')
                            break
                    else:
                        return ('W', word)

        elif decision == "L":

            while True:
                letter = input('Please enter a letter: ').upper()
                if letter in legal and len(letter) ==1:
                    return ('L', letter)
                else:
                    print("I said letter, didn't I?")
        else:
            print('Incorrect input. Please try again.')


def playgame():
    '''Let's user play a single round of handman game'''

    life = LIFE
    capital = pick_cap()
    guessed = []
    incorrect = []
    start_time = time.time()
    win = False

    print("I'm thinking of a capital that is " + str(len(capital)) + " letters long.")
    print(capital)

    while life > 0:
        print()
        display(capital, guessed)

        if incorrect:
            print('\nIncorrect guesses: ' + str(incorrect))

        print('\nLife = ' + str(life))

        (option, guess) = decision()

        if option == 'W':
            if guess == capital:
                win = True
                break
            else:
                life -= 2
                print('WRONG!!!')
                hangman(life)


        else:
            if guess in guessed:
                print('You have already guessed that!')
            elif guess in capital:
                print('Good guess!')
                guessed.append(guess)
                if check_win(guessed,capital):
                    win = True
                    break
            else:
                print('That letter is not in this word!')
                incorrect.append(guess)
                guessed.append(guess)
                life -= 1
                hangman(life)


    else:
        print('YOU HAVE LOST. You should catch up on your geography!\nThe correct answer is: ' + str(capital) + '.')


    if win:
        print("\nThat's right! " +str(capital) + ' is the answer.')
        game_time = round(time.time() - start_time)
        print('You guessed after ' + str(len(guessed)) + ' letters. It took you ' + str(game_time) + ' seconds.')





def playagain(to_be_continued):
    while True:
        answer = input('\nDo you want to play again? Y/N ').upper()
        if answer != 'N' and answer != 'Y':
            print('Incorrect input. Please try again.')
        else:
            if answer == 'N':
                to_be_continued = False
            return to_be_continued


def hangman(life):
    if life == 6:
        print ("________      ")
        print ("|      |      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif life == 5:
        print ("|             ")
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|             ")
        print ("|             ")
        print ("|             ")
    elif life == 4:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /       ")
        print ("|             ")
        print ("|             ")
    elif life == 3:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|      ")
        print ("|             ")
        print ("|             ")
    elif life == 2:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|             ")
        print ("|             ")
    elif life == 1:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     /       ")
        print ("|             ")
    else:
        print ("________      ")
        print ("|      |      ")
        print ("|      0      ")
        print ("|     /|\     ")
        print ("|     / \     ")
        print ("|             ")


def main():

    print('''
 _______ _            _   _
|_     _| |          | | | |
  |   | | |__   ___  | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __
  |   | | '_ \ / _ \ |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
  |   | | | | |  __/ | | | | (_| | | | | (_| | | | | | | (_| | | | |
  \_|_/ |_| |_|\___| \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
    '                                   __/ |
    '                                  |___/
     ''')

    print('Welcome to game, the Hangman!')

    to_be_continued = True

    while to_be_continued:
        playgame()
        to_be_continued = playagain(to_be_continued)


if __name__ == '__main__':
    main()
