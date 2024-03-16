import math
from random import randint


def brain_gcd(number_a, number_b):
    result = math.gcd(number_a, number_b)
    question = [str(number_a), str(number_b)]
    question = " ".join(question)
    return question, str(result)


def generate_question_result_rule():
    rules = 'Find the greatest common divisor of given numbers.'
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    question, result = brain_gcd(number_a, number_b)
    return question, result, rules
