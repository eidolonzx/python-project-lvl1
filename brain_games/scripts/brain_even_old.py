#!/usr/bin/env python
import prompt
import random


def main():
    print("Welcome to the Brain Games!!!")
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_loop(0, name)


def game_loop(counter, name):
    n = random.randint(1, 99)
    print("Question:", n)
    answer = prompt.string("Your answer: ")
    is_correct = n % 2 == 0 and answer == "yes" or n % 2 != 0 and answer == "no"
    if is_correct:
        print("Correct!")
        counter += 1
        # game victory condition is here
        if counter == 3:
            print(f"Congratulations, {name}!")
        else:
            game_loop(counter, name)
    else:
        if answer == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again,", name)


if __name__ == '__main__':
    main()
