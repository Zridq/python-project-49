import prompt
from brain_games.cli import welcome_user


def run_game(sending_question_result, rules):
    name = welcome_user()
    print(rules)
    counter = 0
    rounds = 3
    while counter < rounds:
        question, result = sending_question_result()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            counter += 1
        else:
            print("'" + answer + "'", "is wrong answer ;(. Correct answer \
was", "'" + result + "'" + ".\nLet's try again,", name + "!")
            counter = 5
    if counter == 3:
        print('Congratulations, ' + name + '!')
