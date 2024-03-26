from brain_games.engine import comparing
from brain_games.games.calc import generate_question_result


def main():
    rules = 'What is the result of the expression?'
    comparing(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
