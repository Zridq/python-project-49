from brain_games.engine import comparing
from brain_games.games.even import generate_question_result


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    comparing(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
