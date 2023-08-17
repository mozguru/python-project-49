from random import randint, choice

GAME_QUESTION = 'What number is missing in the progression?'


def brain_progression(start, step, length):
    progression_list = []
    i = 0
    while i < length:
        progression_list.append(start + step * i)
        i += 1
    return progression_list


def game_start():
    start_number = randint(0, 100)
    step_number = randint(1, 10)
    length_number = randint(5, 10)
    progression = brain_progression(start_number, step_number, length_number)
    progression_string = ' '.join(str(n) for n in progression)
    true_answer = choice(progression)
    question = progression_string.replace(str(true_answer), '..', 1)
    return question, str(true_answer)
