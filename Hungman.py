import random
import string
from words import words
from Lives_visual import lives_visual_dict
from About import info


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def Hungman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6
    print(info)
    while len(word_letters) > 0 and lives > 0:
        print('you have', lives,
              'lives left and you have used these letters : ', ''.join(used_letter))

        word_list = [
            letter if letter in used_letter else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current  word : ', ''.join(word_list))

        user_letter = input("Guess Letter : ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1

        elif user_letter in used_letter:
            print('You have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

        if lives == 0:
            print(lives_visual_dict[lives])
            print("you Die")
        else:
            print('YAY! You guessed the word', word, '!!')


Hungman()
