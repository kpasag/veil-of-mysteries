"""
Kyle Pasag
A01428389

Module for boss encounters and challenge mechanics.

This module manages the placement and properties of all bosses,
and implements the interactive mini-games the player must complete
to defeat them. It handles win and loss outcomes for encounters and
keeps track of boss state as the player progresses.
"""
import messages
import random
import player
from typing import Callable, Generator


def generate_boss_positions(board: dict[tuple[int, int], str]) \
        -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    """
    Select three unique positions on the board for boss placement.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :precondition: board must contain at least three valid coordinate keys
    :postcondition: generate three separate coordinates not equal to the starting position (0, 0)
    :return: a tuple containing three (row, column) coordinate tuples
    """
    possible_positions = list(board.keys())
    possible_positions.remove((0, 0))
    boss_one_pos = random.choice(possible_positions)
    possible_positions.remove(boss_one_pos)
    boss_two_pos = random.choice(possible_positions)
    possible_positions.remove(boss_two_pos)
    boss_three_pos = random.choice(possible_positions)
    return boss_one_pos, boss_two_pos, boss_three_pos


def generate_bosses(board: dict[tuple[int, int], str]) -> tuple[dict[str, int | str | bool], ...]:
    """
    Create the three boss dictionaries and assign each a position.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :precondition: board must contain at least three valid coordinate keys
    :postcondition: returns three boss dictionaries with name, alive status, coordinates, and required level
    :return: a tuple of boss dictionaries
    """
    boss_one_pos, boss_two_pos, boss_three_pos = generate_boss_positions(board)
    boss_one = {
        "name": "Enzo, the Winner", "X-coordinate": boss_one_pos[0], "Y-coordinate": boss_one_pos[1],
        "alive": True, "Level_required": 1
    }
    boss_two = {
        "name": "Hvin, Mr. Pride", "X-coordinate": boss_two_pos[0], "Y-coordinate": boss_two_pos[1],
        "alive": True, "Level_required": 2
    }
    boss_three = {
        "name": "Amon, the God of Mischief", "X-coordinate": boss_three_pos[0], "Y-coordinate": boss_three_pos[1],
        "alive": True, "Level_required": 3
    }
    return boss_one, boss_two, boss_three


def fight_boss(character: dict[str, int], boss: dict[str, int | str | bool],
               dialogue: dict[str, Generator[str, None, None]]) -> None:
    if boss["alive"] and boss["Level_required"] <= character["Level"]:
        messages.type_text(messages.colorize_text(f"{{RED}}You are in the presence of {boss["name"]}.{{GREY}}"))
        if boss["name"] == "Enzo, the Winner":
            dice_duel(character, boss, dialogue)
        elif boss["name"] == "Hvin, Mr. Pride":
            wordle(character, boss, dialogue)
        else:
            anagram_game(character, boss, dialogue)
    elif boss["alive"]:
        messages.type_text(messages.colorize_text(f"{{RED}}You are in the presence of {boss["name"]}."))
        level = messages.colorize_text(f"Level too low. Come back if you're level {boss["Level_required"]}{{GREY}}")
        messages.type_text(level)
    else:
        messages.type_text(messages.colorize_text(f"{{BLUE}}{boss["name"]} has already been defeated.{{GREY}}"))


def check_for_foes() -> bool:
    """
    Determine whether the player encounters a foe after making a move.

    :postcondition: prints an encounter description or ambient background message
                    depending on the random outcome
    :return: True if a foe is encountered, False otherwise
    """
    roll = random.randint(1, 10)
    if roll == 10:
        messages.type_text("\033[93mTime freezes. A \033[95mman\033[93m appears from the darkness, "
                           "adjusts his\033[95m monocle\033[93m and smiles at you.\033[0m")
        return True
    else:
        backgrounds = []
        message = messages.get_list_of_message_from_json("ambience")
        for line in message:
            backgrounds.append(messages.colorize_text(line))
        print(random.choice(backgrounds))
        return False


def guessing_game(character: dict[str, int], dialogue: dict[str, Generator[str, None, None]]) -> None:
    """
    """
    secret_number = random.randint(1, 5)
    while True:
        messages.type_text(f'"\033[95mLet’s play a little game,\033[0m" The \033[95mman\033[0m says softly. '
                           f'"\033[95mGuess a number from {1} to {5}.\033[0m"\n')
        guess = input(f'Enter your choice: ')
        if not guess.isdigit():
            print("\033[95mTry again.\033[0m")
            continue
        guess = int(guess)
        if guess < secret_number or guess > secret_number:
            messages.type_text(f'\033[95mHe\033[0m smiles faintly. "\033[95mClose. the number was {secret_number}."')
            player_lose_hp(character, dialogue)
            break
        else:
            messages.type_text('"\033[92mCorrect... You truly are interesting,\033[0m" The \033[95mman\033[0m says.')
            break


def player_lose_hp(character: dict[str, int], dialogue: dict[str, Generator[str, None, None]]) -> None:
    character["Current HP"] -= 1
    messages.type_text(f"\033[91mYou lost one HP. \nHP left: {character["Current HP"]}\033[0m", 0.01)
    messages.type_text(next(dialogue["player_lose_hp"]))


def input_feedback(answer: str, user_guess: str) -> None:
    guess_feedback = ""
    for index in range(len(answer)):
        if user_guess[index] == answer[index]:
            guess_feedback += "{GREEN}" + user_guess[index]
        else:
            if user_guess[index] in answer:
                guess_feedback += "{YELLOW}" + user_guess[index]
            else:
                guess_feedback += "{GREY}" + user_guess[index]
    print(messages.colorize_text(guess_feedback.upper() + "{GREY}"))


def boss_defeated(character: dict[str, int], boss: dict[str, int | str | bool],
                  dialogue: dict[str, Generator[str, None, None]]) -> None:
    character["Level"] += 1
    character["Current HP"] += 1 + boss["Level_required"]
    boss["alive"] = False
    messages.type_text(next(dialogue["boss_defeated"]))
    messages.type_text(next(dialogue["victory_cycle"]))


def wordle(character: dict[str, int], boss: dict[str, int | str | bool],
           dialogue: dict[str, Generator[str, None, None]]) -> None:
    messages.type_text(next(dialogue["Hvin_intro"]))
    messages.type_text(messages.colorize_text(f"{{BLUE}}{boss["name"]} challenges you to a game of wordle!{{GREY}}"))
    answers = messages.get_text_from_txt_file("answers.txt")
    answer = random.choice(answers)
    attempt = 0
    while attempt < 6:
        if play_round(answer):
            print(messages.colorize_text(f"{{GREEN}}Correct! {answer.upper()} was right!{{GREY}}"))
            boss_defeated(character, boss, dialogue)
            return
        attempt += 1
    player_lose_hp(character, dialogue)
    if not player.is_alive(character):
        return
    ask_retry(character, boss, wordle, dialogue)


def ask_retry(character: dict[str, int], boss: dict[str, int | str | bool], function: Callable[
    [dict[str, int], dict[str, int | str | bool], dict[str, Generator[str, None, None]]], None],
              dialogue: dict[str, Generator[str, None, None]]) -> None:
    user_input = input("Try again? (y/n): ").lower().strip()
    try:
        valid = user_input[0]
    except IndexError:
        messages.type_text("Please enter Y or N.")
        ask_retry(character, boss, function, dialogue)
    else:
        if valid == "y":
            function(character, boss, dialogue)
        elif valid == "n":
            return
        else:
            print("Invalid choice. Please enter Y or N.")
            ask_retry(character, boss, function, dialogue)


def play_round(answer: str) -> bool:
    user_guess = input(f"Enter your {len(answer)}-letter guess: ").lower().strip()
    if len(user_guess) != len(answer):
        print(f"Guess must be exactly {len(answer)} letters!")
        return False
    if user_guess == answer:
        return True
    input_feedback(answer, user_guess)
    return False


def anagram_game(character: dict[str, int], boss: dict[str, int | str | bool],
                 dialogue: dict[str, Generator[str, None, None]]) -> None:
    messages.type_text(next(dialogue["Amon_intro"]))
    messages.type_text(messages.colorize_text(f"{{PURPLE}}{boss["name"]} challenges you to a game of anagram!{{GREY}}"))
    answers = messages.get_text_from_txt_file("anagrams.txt")
    answer = random.choice(answers)
    scrambled = "".join(random.sample(answer, len(answer)))
    attempts = 0
    print(f"\nThe letters rearrange:  {scrambled.upper()}")
    while attempts < 5:
        if play_round(answer):
            print(messages.colorize_text(f"{{GREEN}}You restored the true word: {answer.upper()}!{{GREY}}"))
            boss_defeated(character, boss, dialogue)
            return
        attempts += 1
    player_lose_hp(character, dialogue)
    if not player.is_alive(character):
        return
    ask_retry(character, boss, anagram_game, dialogue)


def play_dice_round() -> int:
    player_roll = random.randint(1, 6)
    boss_roll = random.randint(1, 6)
    roll_message = f"You rolled:{{CYAN}} {player_roll}{{GREY}} | Boss rolled:{{YELLOW}} {boss_roll}{{GREY}}"
    print(messages.colorize_text(roll_message))
    if player_roll > boss_roll:
        messages.type_text(messages.colorize_text("{GREEN}You win the round!{GREY}"))
        return 1
    if boss_roll > player_roll:
        messages.type_text(messages.colorize_text("{RED}You lose the round!{GREY}"))
        return -1
    messages.type_text("Tie!")
    return 0


def dice_duel(character: dict[str, int], boss: dict[str, int | str | bool],
              dialogue: dict[str, Generator[str, None, None]]) -> None:
    messages.type_text(next(dialogue["Enzo_intro"]))
    messages.type_text(messages.colorize_text(f"{{YELLOW}}{boss["name"]} challenges you to a game of dice!{{GREY}}"))
    player_score, boss_score = dice_duel_rounds()
    if player_score == 2:
        boss_defeated(character, boss, dialogue)
    else:
        player_lose_hp(character, dialogue)
        if not player.is_alive(character):
            return
        ask_retry(character, boss, dice_duel, dialogue)


def dice_duel_rounds() -> tuple[int, int]:
    player_score = 0
    boss_score = 0
    while player_score < 2 and boss_score < 2:
        try:
            input("Press ENTER to roll.")
        except EOFError:
            print("Input failed, auto-rolling.")
        result = play_dice_round()
        if result == 1:
            player_score += 1
        elif result == -1:
            boss_score += 1
    return player_score, boss_score
