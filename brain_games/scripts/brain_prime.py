#!/usr/bin/env python
from brain_games.gameloop import make_game_loop
import random


game_name = "Brain Prime"
game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    def iterator(counter):
        if number == counter:
            return True
        if number % counter == 0:
            return False
        return iterator(counter + 1)
    return iterator(2)


def game_condition():
    number = random.randint(1, 99)
    question = str(number)
    right_answer = "yes" if is_prime(number) else "no"
    condition = [question, right_answer]
    return condition


def main():
    make_game_loop(game_name, game_rule, game_condition)


if __name__ == '__main__':
    main()
