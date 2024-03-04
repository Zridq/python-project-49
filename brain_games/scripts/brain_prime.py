from random import randint
from brain_games.engine import comparing
from brain_games.cli import welcome_user


def brain_prime():
    question = randint(1, 50)
    if question == 1:
        result = 'no'
        return question, result
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            result = 'no'
            return question, result
    else:
        result = 'yes'
        return question, result


def repeatting():
    counter = 0
    sending = brain_prime()
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = comparing(sending[0], sending[1], name, counter)
    while counter < 3:
        sending = brain_prime()
        counter = comparing(sending[0], sending[1], name, counter)
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    repeatting()
    return


if __name__ == '__main__':
    main()
