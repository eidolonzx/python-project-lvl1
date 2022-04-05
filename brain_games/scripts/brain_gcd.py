#!/usr/bin/env python
from brain_games.gameloop import make_game_loop
import random


game_name = "Brain GCD"
game_rule = "Find the greatest common divisor of given numbers."


def get_gcd(first_num, second_num):
    if first_num == second_num:
        return first_num
    if first_num > second_num:
        return get_gcd(first_num - second_num, second_num)
    return get_gcd(first_num, second_num - first_num)


def game_condition():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = f"{number1} {number2}"
    right_answer = str(get_gcd(number1, number2))
    condition = [question, right_answer]
    return condition


def main():
    make_game_loop(game_name, game_rule, game_condition)


if __name__ == '__main__':
    main()
