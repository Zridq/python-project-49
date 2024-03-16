from random import randint


def building_progression(number_first, lenght, step):
    count = 0
    question = []
    while count < lenght:
        question.append(str(number_first))
        number_first += step
        count += 1
    return question


def making_question(question, number_of_element):
    result = question[number_of_element]
    question[number_of_element] = '..'
    question = " ".join(question)
    return question, result


def generate_question_result_rule():
    number_first = randint(1, 100)
    lenght = randint(11, 20)
    step = randint(1, 20)
    rules = 'What number is missing in the progression?'
    progression = building_progression(number_first, lenght, step)
    number_of_element = randint(0, len(progression) - 1)
    question, result = making_question(progression, number_of_element)
    return question, result, rules
