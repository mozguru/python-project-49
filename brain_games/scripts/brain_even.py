#!/usr/bin/env python3

from random import randint

print('Welcome to the Brain Games!')
print('May I have your name?')
name = input()
print(f"Hello, {name}!")
print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    number = randint(1, 100)
    print('Question: ', number)
    your_answer = input('Your answer: ')
    if number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    if your_answer != true_answer:
        print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
        print("Let's try again!")
    else:
        print('Correct!')


is_even()


def try_count():
    counter = 0
    while counter < 2:
        is_even()
        counter += 1


try_count()
