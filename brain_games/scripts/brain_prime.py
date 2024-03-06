from brain_games.engine import comparing
from brain_games.cli import welcome_user
from brain_games.games.prime import brain_prime


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    comparing(brain_prime, name)
    return


if __name__ == '__main__':
    main()
