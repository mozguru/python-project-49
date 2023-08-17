from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True


def game_start():
    number = randint(1, 100)
    question = f'{number}'
    true_answer = 'yes' if brain_prime(number) else 'no'
    return question, true_answer
