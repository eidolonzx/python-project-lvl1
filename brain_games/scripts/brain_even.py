#!/usr/bin/env python
from brain_games.gameloop import make_game_loop
import random


game_name = "Brain Even"
game_rule = 'Answer "yes" if number even otherwise answer "no"'

def game_condition():
    n = random.randint(1, 99)
    question = n
    right_answer = "yes" if n % 2 == 0 else "no"
    condition = [question, right_answer]
    return condition

def main():
    make_game_loop(game_name, game_rule, game_condition)

if __name__ == '__main__':
    main()
