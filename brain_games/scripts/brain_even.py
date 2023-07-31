#!/usr/bin/env python3

from random import randint

print('Answer "yes" if the number is even, otherwise answer "no".')
print('Question: ', randint(0, 100))
answer = input('Your answer: ')

def check_number(number):
    number = randint(0, 100)
    if number % 2 == 0 and answer == 'yes':
        print('Correct!')
    else:
        print(answer, "is wrong answer ;(. Correct answer was", not answer, "Let's try again")
    return

print(check_number(randint))