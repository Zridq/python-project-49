from random import randint
import random
import operator


def brain_calc(number_a, number_b, op, fn):
    result = fn(number_a, number_b)
    question = [str(number_a), str(op), str(number_b)]
    question = " ".join(question)
    return question, str(result)


def generate_question_result():
    min_number = 1
    max_number = 100
    number_a = randint(min_number, max_number)
    number_b = randint(min_number, max_number)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    op, fn = random.choice(operators)
    question, result = brain_calc(number_a, number_b, op, fn)
    return question, result
