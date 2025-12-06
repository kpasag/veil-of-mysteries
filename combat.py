import messages
import random
from itertools import cycle


def generate_boss_positions(board):
    possible_positions = list(board.keys())
    possible_positions.remove((0, 0))
    boss_one_pos = random.choice(possible_positions)
    possible_positions.remove(boss_one_pos)
    boss_two_pos = random.choice(possible_positions)
    possible_positions.remove(boss_two_pos)
    boss_three_pos = random.choice(possible_positions)
    return boss_one_pos, boss_two_pos, boss_three_pos


def generate_bosses(board):
    boss_one_pos, boss_two_pos, boss_three_pos = generate_boss_positions(board)
    boss_one = {
        "name": "Enzo, the Winner", "X-coordinate": boss_one_pos[0], "Y-coordinate": boss_one_pos[1],
        "alive": True, "Level_required": 1
    }
    boss_two = {
        "name": "Anderson, the Strongest Hunter", "X-coordinate": boss_two_pos[0], "Y-coordinate": boss_two_pos[1],
        "alive": True, "Level_required": 2
    }
    boss_three = {
        "name": "Amon, the God of Mischief", "X-coordinate": boss_three_pos[0], "Y-coordinate": boss_three_pos[1],
        "alive": True, "Level_required": 3
    }
    return boss_one, boss_two, boss_three


def fight_boss(character, boss):
    if boss["alive"] and boss["Level_required"] <= character["Level"]:
        wordle(character, boss)
    elif boss["alive"]:
        print(f"Level too low. Come back if you're level {boss["Level_required"]}")
    else:
        print("This boss has already been defeated.")


def check_for_foes():
    """
    Determine whether the player encounters a foe after making a move.

    :postcondition: prints an encounter description or ambient background message
                    depending on the random outcome
    :return: True if a foe is encountered, False otherwise
    """
    roll = random.randint(1, 10)
    if roll == 10:
        print("\033[93mTime freezes. A \033[95mman\033[93m appears from the darkness, "
              "adjusts his\033[95m monocle\033[93m and smiles at you.\033[0m")
        return True
    else:
        backgrounds = []
        message = messages.get_list_of_message_from_json("ambience")
        for line in message:
            backgrounds.append(messages.colorize_text(line))
        print(random.choice(backgrounds))
        return False


def guessing_game(character):
    """
    Play a number guessing game from the number 1 to 5.

    :param character: a dictionary containing the player's current coordinate and HP
    :precondition: character is a string
    :postcondition: reduces the player's HP by 1 if the answer is incorrect and prints
                    an ambience string based on remaining HP
    """
    secret_number = random.randint(1, 5)
    while True:
        guess = input(f'"\033[95mLet’s play a little game,\033[0m" The \033[95mman\033[0m says softly. '
                      f'"\033[95mGuess a number from {1} to {5}.\033[0m"\n'
                      f'Enter your choice: ')
        if not guess.isdigit():
            print("\033[95mTry again.\033[0m")
            continue
        guess = int(guess)
        if guess < secret_number or guess > secret_number:
            print(f'\033[95mHe\033[0m smiles faintly. "\033[95mClose. the number was {secret_number}."')
            player_lose_hp(character)
            break
        else:
            print('"\033[92mCorrect... You truly are interesting,\033[0m" The \033[95mman\033[0m says.')
            break


def player_lose_hp(character):
    character["Current HP"] -= 1
    lose_hp_message = messages.yield_text_from_json("player_lose_hp")
    print(f"\033[91mYou lost one HP. \nHP left: {character["Current HP"]}\033[0m")
    print(next(lose_hp_message))


def wordle_feedback(answer, user_guess):
    guess_feedback = ""
    for index in range(5):
        if user_guess[index] == answer[index]:
            guess_feedback += "{GREEN}" + user_guess[index]
        else:
            if user_guess[index] in answer:
                guess_feedback += "{YELLOW}" + user_guess[index]
            else:
                guess_feedback += "{GREY}" + user_guess[index]
    print(messages.colorize_text(guess_feedback.upper() + "{GREY}"))


def boss_defeated(character, boss):
    character["Level"] += 1
    boss["alive"] = False


def wordle(character, boss):
    answers = messages.get_text_from_txt_file("answers.txt")
    answer = random.choice(answers)
    attempt = 0
    while attempt < 6:
        user_guess = input("Enter your guess: ").lower()
        if user_guess == answer:
            text = f"{{GREEN}}Correct! Your answer {answer.upper()} was correct. You have defeated Amon{{GREY}}"
            print(messages.colorize_text(text))
            boss_defeated(character, boss)
            break
        else:
            wordle_feedback(answer, user_guess)
        attempt += 1
    if attempt >= 6:
        player_lose_hp(character)