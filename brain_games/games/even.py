from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even_number(number):
    if number % 2 == 0:
        return number


def get_question_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    true_answer = 'yes' if is_even_number(number) else 'no'
    return str(question), true_answer
