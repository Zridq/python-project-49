
import math
from random import randint
from brain_games.engine import comparing
from brain_games.cli import welcome_user


def brain_gcd():
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    result = math.gcd(number_a, number_b)
    question = [str(number_a), str(number_b)]
    question = " ".join(question)
    return question, result


def repeatting():
    counter = 0
    sending = brain_gcd()
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = comparing(sending[0], sending[1], name, counter)
    while counter < 3:
        sending = brain_gcd()
        counter = comparing(sending[0], sending[1], name, counter)
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    repeatting()
    return


if __name__ == '__main__':
    main()
