from brain_games.engine import run_game
from brain_games.games.progression import generate_question_result


def main():
    rules = 'What number is missing in the progression?'
    run_game(generate_question_result, rules)
    return


if __name__ == '__main__':
    main()
