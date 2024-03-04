from random import randint
from brain_games.engine import comparing
from brain_games.cli import welcome_user


def brain_even():
    question = randint(1, 100)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result


def repeatting():
    counter = 0
    sending = brain_even()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = comparing(sending[0], sending[1], name, counter)
    while counter < 3:
        sending = brain_even()
        counter = comparing(sending[0], sending[1], name, counter)
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    repeatting()
    return


if __name__ == '__main__':
    main()
