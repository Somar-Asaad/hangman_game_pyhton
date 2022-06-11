import random
import string
from hangman_visual import lives_visual_dict
from words import words


def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def play():
    word = get_valid_word()
    word_letters = set(word)
    alpha_letters = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(f"you have chosen these letters {used_letters}")
        show = [letter if letter in used_letters else '-' for letter in word]
        print(show)
        user_letters = input("enter a letter to guess").upper()
        if user_letters in alpha_letters - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print(lives_visual_dict[lives])
        elif user_letters in used_letters:
            print("you have already used this letter try again")
        else:
            print("this is not a valid input please try again ")

    if word == 0:
        print("you won!")
    else:
        print("you lost!")


play()
