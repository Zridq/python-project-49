from random import randint


def build_progression(initial_term, elements_in_total, common_difference):
    count = 0
    progression = []
    while count < elements_in_total:
        progression.append(initial_term)
        initial_term += common_difference
        count += 1
    return progression


def make_result(progression, number_of_element):
    result = progression[number_of_element]
    return str(result)


def make_question(progression, number_of_element):
    question = progression.copy()
    question[number_of_element] = '..'
    result = " ".join(map(str, question))
    return result


def generate_question_result():
    min_initial_term = 1
    max_initial_term = 100
    min_elements_in_total = 11
    max_elements_in_total = 20
    min_common_difference = 1
    max_common_difference = 20
    initial_term = randint(min_initial_term, max_initial_term)
    elements_in_total = randint(min_elements_in_total, max_elements_in_total)
    common_difference = randint(min_common_difference, max_common_difference)
    progression = build_progression(initial_term,
                                    elements_in_total,
                                    common_difference)
    number_of_element = randint(0, len(progression) - 1)
    question = make_question(progression, number_of_element)
    result = make_result(progression, number_of_element)
    return question, result
