import json
import random
import string

file = open('words.json')
words_list = json.load(file)
words = words_list['data']

def valid_word():
    temp = words[random.randint(0, len(words))]
    while '-' in temp or ' ' in temp:
        temp = words[random.randint(0, len(words))]
    return temp


def run():
    answer = valid_word().upper()
    word_letters = set(answer)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    attempt_amount = 0
    print(answer)

    while len(word_letters) > 0:
        print('Letter that have been used', ' '.join(used_letters))


        word_list = [letter if letter in used_letters else '-' for letter in answer]
        print('Current word: ', ' '.join(word_list))


        guess = input("Guess a letter: ").upper()
        print('\n')
        attempt_amount+=1
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)

        elif guess in used_letters:
            print('Letter already guessed\n')

        else:
            print('Invalid, please type in an English letter\n')
    print('CONGATULATIONS! YOU GOT IT!')
    print('THE WORD WAS: ', answer)
    print('THIS WORD TOOK YOU ' + str(attempt_amount) + ' ATTEMPTS TO GUESS')

run()

file.close()
