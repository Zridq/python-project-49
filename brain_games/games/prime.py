from random import randint


def is_prime(question):
    if question == 1:
        return False
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return False
    else:
        return True


def generate_question_result():
    min_number = 1
    max_number = 50
    question = randint(min_number, max_number)
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result
