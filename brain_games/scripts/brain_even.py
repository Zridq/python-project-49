from brain_games.engine import comparing
from brain_games.cli import welcome_user
from brain_games.games.even import brain_even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    comparing(brain_even, name)
    return


if __name__ == '__main__':
    main()
