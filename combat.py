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
        backgrounds = ["A\033[95m woman\033[0m passes by, her gaze sharp behind a\033[95m monocle\033[0m.",
                       "You turn your head, and for a moment,"
                       "\033[95m your reflection\033[0m wears a\033[95m monocle\033[0m.",
                       "You glimpse a\033[95m tall man\033[0m with a\033[95m monocle\033[0m"
                       " down the corridor... then he’s gone.",
                       "A\033[95m figure\033[0m with a hat and a flash of\033[95m glass at his eye\033[0m passes by...",
                       "Your\033[95m shadow\033[0m tilts its head and\033[95m adjusts something\033[0m near its eye.",
                       "A\033[95m crow\033[0m lands nearby, a small\033[95m glint of glass\033[0m over one eye.",
                       "A\033[95m cat\033[0m stares at you, a faint\033[95m light glimmering in its pupil.\033[0m"]
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
            character["Current HP"] -= 1
            print(f"\033[91mYou lost one HP. \nHP left: {character["Current HP"]}\033[0m")
            if character["Current HP"] == 4:
                print("A chill seeps into\033[95m your thoughts\033[0m, and one of them no longer feels like yours.")
            elif character["Current HP"] == 3:
                print("\033[95mYour reflection\033[0m lags behind your movement — half a second late.")
            elif character["Current HP"] == 2:
                print("You hear\033[95m faint laughter\033[0m echo inside your skull. It sounds exactly like you.")
            elif character["Current HP"] == 1:
                print("\033[95mYour pulse\033[0m skips —\033[95m someone else’s heartbeat\033[0m matches yours.")
            break
        else:
            print('"\033[92mCorrect... You truly are interesting,\033[0m" The \033[95mman\033[0m says.')
            break


def wordle(character):
    pass