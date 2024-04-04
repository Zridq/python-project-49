import math
from random import randint


def generate_question_result():
    min_number = 1
    max_number = 100
    number_a = randint(min_number, max_number)
    number_b = randint(min_number, max_number)
    result = math.gcd(number_a, number_b)
    question = [str(number_a), str(number_b)]
    question = " ".join(question)
    return question, str(result)
