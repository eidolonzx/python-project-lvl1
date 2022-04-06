#!/usr/bin/env python
from brain_games.gameloop import make_game_loop
import random


game_name = "Brain Progression"
game_rule = "What number is missing in this progression?"


def make_progression(first_num, step, unknown_pos, prog_length):
    def iterator(counter, acc):
        if counter > prog_length - 1:
            return acc
        if counter == unknown_pos:
            current_num_str = ".."
        else:
            current_num_str = str(first_num + counter * step)
        if counter == 0:
            return iterator(counter + 1, f"{current_num_str}")
        return iterator(counter + 1, f"{acc} {current_num_str}")
    return iterator(0, "")


def game_condition():
    prog_length = 10
    step = random.randint(2, 5)
    first_num = random.randint(1, 99)
    unknown_pos = random.randint(1, 9)
    question = make_progression(first_num, step, unknown_pos, prog_length)
    right_answer = str(first_num + unknown_pos * step)
    condition = [question, right_answer]
    return condition


def main():
    make_game_loop(game_name, game_rule, game_condition)


if __name__ == '__main__':
    main()
