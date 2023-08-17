from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even(number):
    if number % 2 == 0:
        return number


def game_start():
    number = randint(1, 100)
    question = number
    true_answer = 'yes' if brain_even(number) else 'no'
    return str(question), true_answer
