from random import randint
import random
import operator


def brain_calc():
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    op, fn = random.choice(operators)
    result = fn(number_a, number_b)
    question = [str(number_a), str(op), str(number_b)]
    question = " ".join(question)
    return question, result
