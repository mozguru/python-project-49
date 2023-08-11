from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def brain_gcd(number_one, number_two):
    while number_one != number_two:
        if number_one > number_two:
            number_one = number_one - number_two
        else:
            number_two = number_two - number_one
    return number_two


def game_start():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    question = f'{number_one} {number_two}'
    true_answer = brain_gcd(number_one, number_two)
    return question, str(true_answer)
