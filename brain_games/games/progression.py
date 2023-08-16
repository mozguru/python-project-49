from random import randint, choice

GAME_QUESTION = 'What number is missing in the progression?'


def brain_progression(start, stop, step):
    length = 10
    progression_list = list(range(start, stop, step))
    return progression_list[:length]


def game_start():
    start_number = randint(1, 50)
    stop_number = randint(50, 100)
    step_number = randint(1, 5)
    progression = brain_progression(start_number, stop_number, step_number)
    progression_string = ' '.join(str(n) for n in progression)
    correct_answer = choice(progression)
    question = progression_string.replace(str(correct_answer), '..')
    return question, str(correct_answer)
