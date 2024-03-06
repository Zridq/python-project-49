from brain_games.engine import comparing
from brain_games.cli import welcome_user
from brain_games.games.calc import brain_calc


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    comparing(brain_calc, name)
    return


if __name__ == '__main__':
    main()
