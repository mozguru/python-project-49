#!/usr/bin/env python3

def main():
    if __name__ == '__main__':
        main()

from random import randint


def brain_even_game():
    print('Welcome to the Brain Games!')
    print('May I have your name?')
    name = input()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print('Question: ', number)
        your_answer = input('Your answer: ')

        if number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        if your_answer == true_answer:
            print('Correct!')
            counter += 1

        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            print("Let's try again!")
            break

    if counter == 3:
        print(f"Congratulations, {name}!")


brain_even_game()
