import prompt


def comparing(question, result, name, counter):
    result = str(result)
    print('Question:', question)
    answer = prompt.string('Your answer: ')
    if result == answer:
        print('Correct!')
        counter += 1
        return counter
    else:
        print("'" + answer + "'", "is wrong answer ;(. Correct answer \
    was", "'" + result + "'", ".\nLet's try again,", name, "!")
        counter = 5
        return counter
