from random import randint


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = randint(1, 100)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result
