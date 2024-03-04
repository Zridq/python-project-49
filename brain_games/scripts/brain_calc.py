from random import randint
import random
import operator
from brain_games.engine import comparing
from brain_games.cli import welcome_user


def brain_calc():
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    op, fn = random.choice(operators)
    result = fn(number_a, number_b)
    question = [str(number_a), str(op), str(number_b)]
    question = " ".join(question)
    return question, result


def repeatting():
    counter = 0
    sending = brain_calc()
    name = welcome_user()
    print('What is the result of the expression?')
    counter = comparing(sending[0], sending[1], name, counter)
    while counter < 3:
        sending = brain_calc()
        counter = comparing(sending[0], sending[1], name, counter)
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    repeatting()
    return


if __name__ == '__main__':
    main()
