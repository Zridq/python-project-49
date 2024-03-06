from random import randint


def brain_progression():
    number_first = randint(1, 100)
    lenght = randint(11, 20)
    step = randint(1, 20)
    count = 0
    question = []

    while count < lenght:
        question.append(str(number_first))
        number_first += step
        count += 1

    number_of_element = randint(0, lenght - 1)
    result = question[number_of_element]
    question[number_of_element] = '..'
    question = " ".join(question)
    return question, result
