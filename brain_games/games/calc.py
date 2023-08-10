#!/usr/bin/env python3

from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'

def brain_calc(number_one, number_two, operator):
    if operator == '+':
        true_answer = number_one + number_two
    elif operator == '*':
        true_answer = number_one * number_two
    elif operator == '-':
        true_answer = number_one - number_two
    return true_answer

def game_start():
    number_one = randint(1, 50)
    number_two = randint(1, 50)
    operator = choice(['+', '*', '-'])
    question = f'{number_one} {operator} {number_two}'
    true_answer = brain_calc(number_one, number_two, operator)
    return question, str(true_answer)
