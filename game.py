"""
Kyle Pasag
A01428389

A single-player, text-based game based on the Lord of the Mysteries novel.
The player starts with 5 hp and begins at the top-left of a 5x5 board (0,0). The player moves using:
'N' for north, 'E' for east, 'W' for west, or 'S' for south. The main goal of the player
is to reach the bottom-right corner of the board (4,4) while surviving occasional encounters from a
foe. If the foe is not beaten in an encounter, the player will lose 1 hp. The game ends when the player's
HP reaches zero or when the player reaches the goal.
"""
import random
import combat
import player


def welcome():
    print("H")


def game():
    """
    Initializes the game board and the player character, then continuously processes
    player input for movement until the game ends.

    :precondition: all helper functions must be defined and working as intended
    :postcondition: run the entire game sequence, while continuously prompting the user for input
                    for the player movement until one of the two endings have been met: victory
                    or defeat
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = player.make_character()
    achieved_goal = False
    describe_current_location(board, character)
    while is_alive(character) and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            player.move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                combat.guessing_game(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Please try again.")
    if is_alive(character) and achieved_goal:
        print("\033[92m" + r"""
            __     __                    _       
            \ \   / /                   (_)      
             \ \_/ /__  _   _  __      ___ _ __  
              \   / _ \| | | | \ \ /\ / / | '_ \ 
               | | (_) | |_| |  \ V  V /| | | | |
               |_|\___/ \__,_|   \_/\_/ |_|_| |_|

                                      """)
        print("You have reached the end. For now, your mind is your own.\033[0m")
    if not is_alive(character):
        print("\033[91m" + r"""
           _____          __  __ ______    ______      ________ _____  
          / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
         | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
         | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
         | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
          \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\

        """ + "\033[0m")
        print("\033[95mYou smile. It’s not your smile anymore.")
        print("Your hand rises on its own, adjusting a monocle that isn't yours.")
        print("There is no you now. Only him.")
        print('"Perfect." a voice says from inside your mouth.\033[0m')


def describe_current_location(board, character):
    """
    Display the current location of the player and the room description of the coordinates they're in.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary containing the player's current coordinate and HP
    :precondition: the board must contain valid keys that match the character's position
    :postcondition displays the player's current location and the room description
    >>> my_board = {(0, 0): "Silent Room", (0, 1): "Dark Hallway"}
    >>> describe_current_location(my_board, {"X-coordinate": 0, "Y-coordinate": 1})
    Current Location: \033[94m(0,1)\033[0m
    You step into the Dark Hallway.
    >>> describe_current_location(my_board, {"X-coordinate": 0, "Y-coordinate": 0})
    Current Location: \033[94m(0,0)\033[0m
    You step into the Silent Room.
    """
    char_x_coordinate = character["X-coordinate"]
    char_y_coordinate = character["Y-coordinate"]
    location = board[(char_x_coordinate, char_y_coordinate)]
    print(f"Current Location: \033[94m({char_x_coordinate},{char_y_coordinate})\033[0m")
    print(f"You step into the {location}.")


def get_user_choice():
    """
    Prompts the player for a direction to move.

    :postcondition: lower cases the players input and removes extra spaces in-between
    :return: the adjusting input as a string
    """
    return input("Which way will you go?\n"
                 "'\033[96mN\033[0m' for north, '\033[96mE\033[0m' for east,"
                 "'\033[96mW\033[0m' for west, or '\033[96mS\033[0m' for south.\n"
                 "Enter your choice: ").lower().strip()


def validate_move(board, character, direction):
    """
    Check whether the player's input for movement is valid.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary containing the player's current coordinate and HP
    :param direction: a lowercase string representing the movement direction
                      ('n', 'e', 'w', or 's')
    :precondition: board is a dictionary, character is a dictionary, and direction is a string
    :postcondition: checks if the direction is within the boundaries of the board and if it
                    is one of the four valid directions ('n', 'e', 'w', or 's')
    :return: True if the direction given is valid, False otherwise

    >>> my_board = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
    >>> my_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(my_board, my_character, "n")
    You can't go further north.
    False
    >>> validate_move(my_board, my_character, "5")
    False
    >>> validate_move(my_board, my_character, "e")
    True
    """
    max_row = max(coordinate[0] for coordinate in board.keys())
    max_col = max(coordinate[1] for coordinate in board.keys())
    if direction == "n":
        if character["X-coordinate"] == 0:
            print("You can't go further north.")
            return False
    elif direction == "e":
        if character["Y-coordinate"] == max_col:
            print("You can't go further east.")
            return False
    elif direction == "w":
        if character["Y-coordinate"] == 0:
            print("You can't go further west.")
            return False
    elif direction == "s":
        if character["X-coordinate"] == max_row:
            print("You can't go further south.")
            return False
    else:
        return False
    return True


def check_if_goal_attained(board, character):
    """
    Check if the player has reached the bottom-right of the board

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary containing the player's current coordinate and HP
    :precondition: board and character are a dictionary
    :postcondition: check if the player's current coordinate matches the goal coordinate
                    which is in the bottom-right corner of the board
    :return: True if the player has reached the goal, False otherwise

    >>> my_board = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Goal Room"}
    >>> my_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> check_if_goal_attained(my_board, my_character)
    False
    >>> my_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> check_if_goal_attained(my_board, my_character)
    True
    """
    max_row = max(coordinate[0] for coordinate in board.keys())
    max_col = max(coordinate[1] for coordinate in board.keys())
    char_x_coord = character["X-coordinate"]
    char_y_coord = character["Y-coordinate"]
    return (max_row, max_col) == (char_x_coord, char_y_coord)


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


def is_alive(character):
    """
    Check whether the player is still alive based on their current HP.

    :param character: a dictionary containing the player's current coordinate and HP
    :precondition: character is a string
    :postcondition: determine if the player is still alive or not based on their HP
    :return: True if the player HP is greater than 0, False otherwise

    >>> my_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> is_alive(my_character)
    True
    >>> my_character["Current HP"] = 0
    >>> is_alive(my_character)
    False
    """
    return character["Current HP"] != 0


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()