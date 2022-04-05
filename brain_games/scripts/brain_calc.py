#!/usr/bin/env python
from brain_games.gameloop import make_game_loop
import random


game_name = "Brain Calc"
game_rule = "What is the result of the expression?"


def game_condition():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation_number = random.randint(1, 3)
    if operation_number == 1:
        operation = "+"
        right_answer = str(first_number + second_number)
    elif operation_number == 2:
        operation = "-"
        right_answer = str(first_number - second_number)
    else:
        operation = "*"
        right_answer = str(first_number * second_number)
    question = f"{first_number} {operation} {second_number}"
    condition = [question, right_answer]
    return condition


def main():
    make_game_loop(game_name, game_rule, game_condition)


if __name__ == '__main__':
    main()
