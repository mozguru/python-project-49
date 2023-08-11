#!/usr/bin/env python3

def game_logic(_):
    print('Welcome to the Brain Games!')
    print('May I have your name?')
    name = input()
    print(f"Hello, {name}!")

    round_counter = 0
    print(_.GAME_QUESTION)

    win = 3
    while round_counter < win:
        question, true_answer = _.game_start()
        print(f'Question: {question}')
        your_answer = input('Your answer: ')

        if your_answer == true_answer:
            print('Correct!')
            round_counter += 1

        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if round_counter == 3:
        print(f"Congratulations, {name}!")
