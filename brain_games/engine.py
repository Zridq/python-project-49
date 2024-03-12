import prompt
from brain_games.cli import welcome_user


def comparing(sending_question_result):
    name = welcome_user()
    counter = 0
    while counter < 3:
        question, result = sending_question_result()
        result = str(result)
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
