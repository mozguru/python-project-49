from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime_number(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True


def get_question_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number}'
    true_answer = 'yes' if is_prime_number(number) else 'no'
    return question, true_answer
