from random import randint


def brain_even():
    question = randint(1, 100)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result
