from brain_games.engine import comparing
from brain_games.games.gcd import generate_question_result


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    comparing(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
