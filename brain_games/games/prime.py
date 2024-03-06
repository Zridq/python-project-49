from random import randint


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
