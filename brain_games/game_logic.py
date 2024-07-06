def start_game(_):
    print('Welcome to the Brain Games!')
    print('May I have your name?')
    name = input()
    print(f"Hello, {name}!")

    round_counter = 0
    print(_.GAME_QUESTION)

    ROUND_LIMIT = 3

    while round_counter < ROUND_LIMIT:
        question, true_answer = _.get_question_answer()
        print(f'Question: {question}')
        your_answer = input('Your answer: ')

        if your_answer == true_answer:
            print('Correct!')
            round_counter += 1

        else:
            print(f"'{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if round_counter == 3:
        print(f"Congratulations, {name}!")
