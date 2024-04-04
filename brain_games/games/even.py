from random import randint


def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def generate_question_result():
    min_number = 1
    max_number = 100
    question = randint(min_number, max_number)
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result
