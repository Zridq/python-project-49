from random import randint


def building_progression(number_first, lenght, step):
    count = 0
    progression = []
    while count < lenght:
        progression.append(str(number_first))
        number_first += step
        count += 1
    return progression


def making_result(progression, number_of_element):
    result = progression[number_of_element]
    return result


def making_question(progression, number_of_element):
    question = progression.copy()
    question[number_of_element] = '..'
    question = " ".join(question)
    return question


def generate_question_result():
    number_first = randint(1, 100)
    lenght = randint(11, 20)
    step = randint(1, 20)
    progression = building_progression(number_first, lenght, step)
    number_of_element = randint(0, len(progression) - 1)
    question = making_question(progression, number_of_element)
    result = making_result(progression, number_of_element)
    return question, result
