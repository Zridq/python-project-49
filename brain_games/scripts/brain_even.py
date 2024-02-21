from random import randint
import prompt


def main():
    return


if __name__ == '__main__':
    main()

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')
counter = 0

while counter < 3:
    random_number = randint(1, 100)
    print('Question:', random_number)
    answer = prompt.string('Your answer: ')

    if random_number % 2 == 0 and answer == 'yes' or \
            random_number % 2 != 0 and answer == 'no':
        counter += 1
        print('Correct!')
    else:
        if random_number % 2 == 0:
            print(answer, "is wrong answer ;(. Correct answer \
was 'yes'.\nLet's try again", name, "!")
        else:
            print(answer, "is wrong answer ;(. Correct answer \
was 'no'.\nLet's try again", name, "!")
        counter = 5

if counter == 3:
    print('Congratulations, ' + name + '!')
