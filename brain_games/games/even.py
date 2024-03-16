from random import randint


def is_even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def generate_question_result_rule():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result, rules
