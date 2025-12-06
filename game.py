"""
Kyle Pasag
A01428389


"""
import combat
import player
import game_board
import messages


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
    board = game_board.make_board(rows, columns)
    character = player.make_character()
    achieved_goal = False
    json_text_printer("welcome_message")
    describe_current_location(board, character)
    while is_alive(character) and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            player.move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = combat.check_for_foes()
            if there_is_a_challenger:
                combat.check_player_level(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Please try again.")
    if is_alive(character) and achieved_goal:
        json_text_printer("win_message")
    if not is_alive(character):
        json_text_printer("lost_message")


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