import json
import random


def check_for_foes():
    """
    Determine whether the player encounters a foe after making a move.

    :postcondition: prints an encounter description or ambient background message
                    depending on the random outcome
    :return: True if a foe is encountered, False otherwise
    """
    roll = random.randint(1, 4)  # returns an int between 1 and 100
    if roll == 4:
        print("\033[93mTime freezes. A \033[95mman\033[93m appears from the darkness, "
              "adjusts his\033[95m monocle\033[93m and smiles at you.\033[0m")
        return True
    else:
        backgrounds = []
        message = get_player_lose_hp_message("ambience")
        for line in message:
            backgrounds.append(line)
        print(random.choice(backgrounds))
        return False


def check_player_level(character):
    if character["Level"] <= 1:
        guessing_game(character)
    elif character["Level"] <= 2:
        wordle(character)
    elif character["Level"] <= 3:
        pass


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

# Make this reusable
def get_player_lose_hp_message(text):
    with open("messages.json", "r", encoding="utf-8") as data:
        data_object = json.load(data)
        yield from map(lambda text_line: text_line.replace("{PURPLE}", "\033[95m"), data_object)




def player_lose_hp(character):
    character["Current HP"] -= 1
    lose_hp_message = get_player_lose_hp_message("player_lose_hp")
    print(f"\033[91mYou lost one HP. \nHP left: {character["Current HP"]}\033[0m")
    print(next(lose_hp_message))


def wordle(character):
    pass