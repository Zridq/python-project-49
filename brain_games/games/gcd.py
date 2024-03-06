import math
from random import randint


def brain_gcd():
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    result = math.gcd(number_a, number_b)
    question = [str(number_a), str(number_b)]
    question = " ".join(question)
    return question, result
