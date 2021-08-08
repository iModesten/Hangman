# Write your code here
import random
import string

entered_letters = set()


def main_function():
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(list_of_words)
    guessed_word = '-' * len(chosen_word)
    count_of_tries = 8
    while True:
        if count_of_tries != 0 and '-' in guessed_word:
            guessed_word, count_of_tries = guess_function(chosen_word, guessed_word, count_of_tries)
        elif count_of_tries > 0 and '-' not in guessed_word:
            print("You survived!")
            break
        else:
            print("You lost!")
            break
#     print("""\nThanks for playing!
# We'll see how well you did in the next stage""")
    # result = chosen_word[0:3] + '-' * (len(chosen_word) - 3)


def guess_function(chosen_word, guessed_word, count_of_tries):
    print('\n' + guessed_word)
    letter = input('Input a letter: ')
    if len(letter) == 0 or len(letter) > 1:
        print("You should input a single letter")
        return guessed_word, count_of_tries
    elif letter not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
        return guessed_word, count_of_tries
    letters_list = list(chosen_word)
    set_of_word = set(chosen_word)
    if letter in entered_letters:
        print("You've already guessed this letter")
        # count_of_tries -= 1
        # print("No improvements")
        return guessed_word, count_of_tries
    elif letter in set_of_word:
        guessed_word = ''
        entered_letters.add(letter)
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                guessed_word = guessed_word + letter
            elif chosen_word[i] in entered_letters and chosen_word[i] == letters_list[i]:
                guessed_word = guessed_word + letters_list[i]
            else:
                guessed_word = guessed_word + '-'
        return guessed_word, count_of_tries
    else:
        count_of_tries -= 1
        entered_letters.add(letter)
        print("That letter doesn't appear in the word")
        return guessed_word, count_of_tries


def create_menu():
    print("H A N G M A N")
    print('Type "play" to play the game, "exit" to quit: ')
    while True:
        choice = input()
        if choice == 'play':
            main_function()
        elif choice == 'exit':
            break
        else:
            print('Type "play" to play the game, "exit" to quit: ')


create_menu()
