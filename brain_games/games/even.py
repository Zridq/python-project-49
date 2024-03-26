from random import randint


def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def generate_question_result():
    question = randint(1, 100)
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result
