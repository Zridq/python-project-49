from random import randint
from brain_games.engine import comparing
from brain_games.cli import welcome_user


def brain_progression():
    number_first = randint(1, 100)
    lenght = randint(11, 20)
    step = randint(1, 20)
    count = 0
    question = []

    while count < lenght:
        question.append(str(number_first))
        number_first += step
        count += 1

    number_of_element = randint(0, lenght - 1)
    result = question[number_of_element]
    question[number_of_element] = '..'
    question = " ".join(question)
    return question, result


def repeatting():
    counter = 0
    sending = brain_progression()
    name = welcome_user()
    print('What number is missing in the progression?')
    counter = comparing(sending[0], sending[1], name, counter)
    while counter < 3:
        sending = brain_progression()
        counter = comparing(sending[0], sending[1], name, counter)
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    repeatting()
    return
