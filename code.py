"""
Pseudocode:
1. Create 4 lists, each with 20 items of a different category
2. Define ask_user() => will return int num_guesses and list of the category they chose
    ask user to choose a level - reprompt until valid response
    if 'easy':
        tries = 10
    if 'medium':
        tries = 8
    if 'hard':
        tries = 6
    ask user to choose a category
        assign the list based on the users category
    return num_tries, list
3. Define choose_word(list) => returns a string
    choose a random word from the given list
    return the word
4. Create print_list(list):
    loops through the given list
        prints each item in list
        with a space in between
5. Create word_check(list):
    takes in a list and checks if there are any '_' in it
    if '_':
        returns False
    else:
        returns True
    (This checks if the user already guessed all the letters in the word or not)
6. Create print_sorted_list(list)
    prints all the items in the list sorted in alphabetical order
    (used at the end of each guess to let the user know which letters they already guessed)
7. Create guess_letter()
    asks the user to guess a letter, returns that letter
8. Create validate_guess(string)
    This will validate the word returned in guess_letter to make sure it is only 1 single letter
    check using is_char and .strip()
9. Create check_if_repeated(already_guessed, guess)
    Checks if the guess that the user guesses was already guessed in the past or not
    takes in a word and a list
    if the word is already in the list
        it warns the user
        returns false
    else:
        adds the letter to the list
        returns True
10. Create game_loop(num_guesses, word)
    creates an empty list for already guesses letters
    creates a list of '_' based on the number of letter in word
    while num_guesses > 0:
        call guess_letter()
        call validate_guess()
        if validate_guess is false:
            continue
        else:
            if not check_if_repeated():
                continue
            else:
                loops through word:
                    if letter in word == guess
                        correct_guess = True
                        add it to list letters
                if correct_guess == True
                    print 'correct'
                else
                    print 'incorrect'
                    continue
        if they guessed the word:
            return True
        else:
            return False
11. create play_game():
    make a variable wins
    make a variable losses
    in a while loop:
        play game
        if game = True
            wins += 1
        else:
            losses += 1
        aske: do you want to play again
        if yes:
            continue
        else:
            print wins and losses
            break
"""
import random

animals = [
    "zebra", "tiger", "elephant", "monkey", "squirrel",
    "walrus", "manatee", "peacock", 'otter', 'panda',
    'rabbit', 'cheetah', 'hamster', 'octopus', 'giraffe',
    'alligator', 'dolphin', 'buffalo', 'beaver', 'llama'
]
foods = [
    "pizza", "hamburger", "salad", "chicken", "banana",
    "pretzels", "donut", "chocolate", 'pasta', 'yogurt',
    'popcorn', 'cookies', 'sandwich', 'sushi', 'tacos',
    'oatmeal', 'cereal', 'burrito', 'muffins', 'brownie'
]
sports = [
    "skating", "tennis", "basketball", "football", "swimming",
    "dancing", "baseball", "gymnastics", "soccer", "skiing",
    "hockey", "boxing", "softball", "rowing", "surfing",
    "fencing", "bowling", "sailing", "golfing", "lacrosse"
]
colors = [
    "orange", "purple", "yellow", "green", "indigo",
    "violet", "maroon", "peach", "silver", "brown",
    "black", "white", "crimson", "magenta", "turquoise",
    "scarlet", "mustard", "emerald", "lavender", "blue"
]

def ask_user():
    """
    asks the user to choose a level and category
    returns a corresponding number of tries and corresponding list
    """
    num_guesses = 0
    list_choice = []
    while True:
        level = input('Choose level: easy/medium/hard ').lower()
        if level == 'easy' or level == 'medium' or level == 'hard':
            break
        else:
            print('Please enter a valid choice')
            continue
    if level == 'easy':
        num_guesses = 10
    elif level == 'medium':
        num_guesses = 8
    elif level == 'hard':
        num_guesses = 6
    while True:
        category = input('Chooses a category: animals/foods/sports/colors ').lower()
        if category == 'animals':
            list_choice = animals
            break
        elif category == 'foods':
            list_choice = foods
            break
        elif category == 'sports':
            list_choice = sports
            break
        elif category == 'colors':
            list_choice = colors
            break
        else:
            print('Please enter a valid choice')
            continue
    return num_guesses, list_choice


def choose_word(list):
    """
    takes in a list
    chooses a random word from list
    returns that word
    """
    choice = random.choice(list)
    return choice


def print_list(list):
    """
    takes in a list
    prints every item in list with a space in between
    """
    for word in list:
        print(word, end = ' ')
    print()


def word_check(list):
    """
    checks if the user guessed the word
    takes in a list
    if there are no dashes, user has guessed the word - it returns true
    if not - it returns false
    """
    for letter in list:
        if letter == '_':
            return False
    return True


def print_sorted_list(list):
    """
    takes in a list
    prints the list in alphabetical order with spaces between the words
    """
    list.sort()
    for word in list:
        print(word, end = ' ')
    print()


def guess_letter():
    """
    asks a user to guess a letter
    returns the letter
    """
    guess = input('Guess a letter: ').lower()
    return guess


def validate_guess(string):
    """
    makes sure the inputted string is 1 letter, not a number
    returns True if guess meets the requirements
    returns False otherwise
    """
    if not string.isalpha():
        print('Invalid input. Please guess a letter only. ')
        return False
    if len(string) > 1:
        print('Invalid input. Please guess 1 letter only. ')
        return False
    return True


def check_if_repeated(already_guessed, guess):
    """
    checks if the str guess is in list already_guessed
    if it is: returns False
    if not: it adds guess to already_guess and returns True
    """
    if guess in already_guessed:
        print('You already guessed this letter')
        return False
    else:
        already_guessed.append(guess)
        return True


def game_loop(num_guesses, word):
    """
    plays 1 round of the game
    takes in the number of guesses and the word they will have to guess
    returns True if they guess it and False if they don't
    """
    already_guessed = []

    # creates a list of _'s based on the length of word
    letters = ['_'] * len(word)

    # Has the user guess letters until they are out of tries
    while num_guesses > 0:
        guess = guess_letter()
        print()

        # makes sure the guess is 1 letter
        if not validate_guess(guess):
            continue

        # checks if the user repeated a guest - if so, reprompts
        if not check_if_repeated(already_guessed, guess):
            continue

        # sets correct_guess to false, will be changed if it is true
        correct_guess = False

        # if the guess is in the word, changes its value in list letters and sets correct_guess to True
        for i in range(len(word)):
               if word[i] == guess:
                   letters[i] = guess
                   correct_guess = True


        if not correct_guess:
            print('Incorrect! Guess another letter: ')
            num_guesses -= 1
            print('Already guessed: ', end = " ")
            print_sorted_list(already_guessed)
            print(f'You have {num_guesses} tries left. ')
            print_list(letters)
            print()
            continue
        else:
            print('Correct!')
            print('Already guessed: ')
            print_sorted_list(already_guessed)
            print(f'You have {num_guesses} tries left. ')
            print_list(letters)
            print()


        if word_check(letters):
            print(f'You guessed the word!! It was: {word}! ')
            return True
    print()
    print(f'Out of guesses - the word was: {word}')
    print()
    return False


def play_game():
    """
    plays the game until the user doesn't want to anymore
    prints the number of wins and losses
    """
    wins = 0
    loses = 0
    while True:
        num_tries, category = ask_user()
        game = game_loop(num_tries, choose_word(category))
        if game:
            wins += 1
        else:
            loses += 1
        play_again = input('Play again? (y/n)')
        if play_again == 'y':
            continue
        elif play_again == 'n':
            break
        else:
            play_again = input('Play again? ')
    if loses > 0 or wins > 0:
        print(f'You won {wins} games and lost {loses} games')


play_game()





