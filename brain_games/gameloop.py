import prompt


def get_name():
    name = prompt.string("May I have your name? ")
    return name


def do_turn(game_condition, current_turn):
    game_turns = 3
    if current_turn > game_turns:
        return True
    condition = game_condition()    
    question = condition[0]
    right_answer = condition[1]

    print(f"Question: {question}")
    players_answer = prompt.string("Your answer: ")

    if players_answer == right_answer:
        print("Correct!")
    else:
        print(f"{players_answer} is wrong answer ;( Correct answer was {right_answer}")
        return False
    current_turn += 1
    return do_turn(game_condition, current_turn)


def make_game_loop(game_name, game_rule, game_condition):
    print('I am here!')
    print(game_condition)
    print('I am here too!')
    current_turn = 1
    print(f"Welcome to the {game_name}")
    player_name = get_name()
    print(f"Hello, {player_name}")
    print(game_rule)
    is_win = do_turn(game_condition, current_turn)
    if is_win:
        print(f"Congratulations, {player_name}!")
    else:
        print(f"Let's try again, {player_name}!")