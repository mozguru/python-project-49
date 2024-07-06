from random import randint, choice

GAME_QUESTION = 'What number is missing in the progression?'

MIN_FIRST_TERM = 0
MAX_FIRST_TERM = 100
MIN_COMM_DIFF = 1
MAX_COMM_DIFF = 10
MIN_SEQUENCE = 5
MAX_SEQUENCE = 10


def generate_progression(term, diff, length):
    progression_list = []
    i = 0
    while i < length:
        progression_list.append(term + diff * i)
        i += 1
    return progression_list


def get_question_answer():
    first_term = randint(MIN_FIRST_TERM, MAX_FIRST_TERM)
    common_difference = randint(MIN_COMM_DIFF, MAX_COMM_DIFF)
    sequence_length = randint(MIN_SEQUENCE, MAX_SEQUENCE)
    progression = generate_progression(first_term, common_difference, sequence_length)
    progression_string = ' '.join(str(n) for n in progression)
    true_answer = choice(progression)
    question = progression_string.replace(str(true_answer), '..', 1)
    return question, str(true_answer)
