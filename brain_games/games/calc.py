#!/usr/bin/env python3

from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 50


def calc_expression(number_one, number_two, operator):
    if operator == '+':
        true_answer = number_one + number_two
    elif operator == '*':
        true_answer = number_one * number_two
    elif operator == '-':
        true_answer = number_one - number_two
    return true_answer


def get_question_answer():
    number_one = randint(MIN_NUMBER, MAX_NUMBER)
    number_two = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(['+', '*', '-'])
    question = f'{number_one} {operator} {number_two}'
    true_answer = calc_expression(number_one, number_two, operator)
    return question, str(true_answer)
