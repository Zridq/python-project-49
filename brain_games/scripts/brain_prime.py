from brain_games.engine import comparing
from brain_games.games.prime import generate_question_result


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    comparing(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
