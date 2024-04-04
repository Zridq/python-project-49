from brain_games.engine import run_game
from brain_games.games.even import generate_question_result


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
