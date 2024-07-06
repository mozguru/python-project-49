from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def find_gcd(number_one, number_two):
    while number_one != number_two:
        if number_one > number_two:
            number_one = number_one - number_two
        else:
            number_two = number_two - number_one
    return number_two


def get_question_answer():
    number_one = randint(MIN_NUMBER, MAX_NUMBER)
    number_two = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number_one} {number_two}'
    true_answer = find_gcd(number_one, number_two)
    return question, str(true_answer)
