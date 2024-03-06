from brain_games.engine import comparing
from brain_games.cli import welcome_user
from brain_games.games.gcd import brain_gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    comparing(brain_gcd, name)
    return


if __name__ == '__main__':
    main()
