from random import choice
from sys import exit

words = ["basket", "book", "banana", "church", "children", "congratulate", "dance", "government", "kitchen",
         "masculine"]

words_meaning = {'basket': 'Object used to store water',
                 'book': 'You will get knowledge by reading it',
                 'banana': 'A fruit which is favourite of Monkeys as well',
                 'church': 'house of God',
                 'children': 'Every one loves them',
                 'congratulate': 'Word used when someone win',
                 'dance': 'It helps to release stress',
                 'government': "A Body that takes country's decision",
                 'kitchen': 'Area to cook Food',
                 'masculine': 'refer to male people or animals'}


def get_word():
    wrd = choice(words)
    return wrd, words_meaning[wrd]


def greet_user():
    user_name = input("What is your name? ")
    print(f'Good Luck!', user_name)
    print('Guess the characters')
    print('You have 12 chances to guess the word')


def play_game():
    count = 12
    word, word_meaning = get_word()
    word_list = []
    for i in range(len(word)):
        word_list.append('_')
        print('_')
    while count > 0:
        input_char = input(f'{count} chances left\nguess a character (Word Meaning - {word_meaning}) : ').lower()
        if len(input_char) > 1:
            continue
        if input_char in word:
            for index in range(len(word)):
                if word[index] == input_char:
                    word_list[index] = input_char

        for chr in word_list:
            print(chr)

        if '_' not in word_list:
            print('You Win!👏')
            return

        count -= 1

    print('You Loose😔')


if __name__ == '__main__':
    greet_user()
    play_game()
