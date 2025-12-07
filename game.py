"""
Kyle Pasag
A01428389

Main gameplay module for the text-based adventure game.

This module controls the overall execution flow, map display,
movement validation, and win condition checks of the game.
It reads board data and character location information to
provide navigation and progress feedback to the player.
"""
import combat
import player
import game_board
import messages


def game() -> None:
    """
    Initializes the game board and the player character, then continuously processes
    player input for movement until the game ends.

    :precondition: all helper functions must be defined and working as intended
    :postcondition: run the entire game sequence, while continuously prompting the user for input
                    for the player movement until one of the two endings have been met: victory
                    or defeat
    """
    rows, columns = 10, 10
    board = game_board.make_board(rows, columns)
    character = player.make_character()
    bosses = combat.generate_bosses(board)
    dialogues = messages.generate_dialogue()
    achieved_goal = False
    messages.type_text(messages.return_text_from_json("welcome_message"), 0.005)
    display_current_location(character, bosses, rows, columns)
    describe_current_location(board, character)
    while player.is_alive(character) and not achieved_goal:
        direction = messages.get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            player.move_character(character, direction)
            display_current_location(character, bosses, rows, columns)
            describe_current_location(board, character)
            for boss in bosses:
                if boss["X-coordinate"] == character["X-coordinate"] and \
                        boss["Y-coordinate"] == character["Y-coordinate"]:
                    combat.fight_boss(character, boss, dialogues)
            if character["Level"] < 3:
                there_is_a_challenger = combat.check_for_foes()
                if there_is_a_challenger:
                    combat.guessing_game(character, dialogues)
            achieved_goal = check_if_goal_attained(bosses)
    if player.is_alive(character) and achieved_goal:
        messages.type_text(messages.return_text_from_json("win_message"), 0.005)
    if not player.is_alive(character):
        messages.type_text(messages.return_text_from_json("lost_message"), 0.005)


def display_current_location(character: dict[str, int], bosses: tuple[dict[str, int | str | bool], ...], rows: int,
                             columns: int) -> None:
    """
    Display the current map showing player position and boss locations.

    :param character: a dictionary storing X and Y coordinates of the character
    :param bosses: list of boss dictionaries that contain location and alive status
    :param rows: number of rows in the board
    :param columns: number of columns in the board
    :precondition: coordinates must be within valid board dimensions
    :postcondition: prints a map to console
    """
    print("\nMap:")
    for row in range(rows):
        row_display = ""
        for column in range(columns):
            if (column, row) == (character["X-coordinate"], character["Y-coordinate"]):
                row_display += " P"
            else:
                icon = " ."
                for boss in bosses:
                    if boss["alive"] and boss["X-coordinate"] == column and boss["Y-coordinate"] == row:
                        icon = " ?" if boss["Level_required"] > character["Level"] else " B"
                        break
                row_display += icon
        messages.type_text(f" {row_display}", 0.001)


def describe_current_location(board: dict[tuple[int, int], str], character: dict[str, int]) -> None:
    """
    Display the current location of the player and the room description of the coordinates they're in.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary storing X and Y coordinates of the character
    :precondition: the board must contain valid keys that match the character's position
    :postcondition displays the player's current location and the room description
    >>> my_board = {(0, 0): "Silent Room", (0, 1): "Dark Hallway"}
    >>> describe_current_location(my_board, {"X-coordinate": 0, "Y-coordinate": 1})
    Current Location: \033[96m(0,1)\033[0m
    You step into the Dark Hallway.
    >>> describe_current_location(my_board, {"X-coordinate": 0, "Y-coordinate": 0})
    Current Location: \033[96m(0,0)\033[0m
    You step into the Silent Room.
    """
    char_x_coordinate = character["X-coordinate"]
    char_y_coordinate = character["Y-coordinate"]
    location = board[(char_x_coordinate, char_y_coordinate)]
    location_message = f"Current Location: {{CYAN}}({char_x_coordinate},{char_y_coordinate}){{GREY}}"
    messages.type_text(messages.colorize_text(location_message), 0.007)
    messages.type_text(f"You step into the {location}.", 0.01)


def next_position(character: dict[str, int], direction: str) -> tuple[int, int] | None:
    """
    Compute the next board position based on input direction.

    :param character: a dictionary storing X and Y coordinates of the character
    :param direction: a lowercase string representing the movement direction
                      ('w', 'a', 's', or 'd)
    :precondition: character contains "X-coordinate" and "Y-coordinate" keys
    :postcondition: does not modify the character dictionary
    :return: a (row, column) tuple if direction is valid, otherwise None

    >>> next_position({"X-coordinate": 2, "Y-coordinate": 2}, "w")
    (2, 1)
    >>> next_position({"X-coordinate": 2, "Y-coordinate": 2}, "x") is None
    True
    """
    x_position, y_position = character["X-coordinate"], character["Y-coordinate"]
    if direction == "w":
        return x_position, y_position - 1
    elif direction == "s":
        return x_position, y_position + 1
    elif direction == "a":
        return x_position - 1, y_position
    elif direction == "d":
        return x_position + 1, y_position
    else:
        return None


def validate_move(board: dict[tuple[int, int], str], character: dict[str, int], direction: str) -> bool:
    """
    Check whether the player's input for movement is valid.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary storing X and Y coordinates of the character
    :param direction: a lowercase string representing the movement direction
                      ('w', 'a', 's', or 'd)
    :precondition: board is a dictionary, character is a dictionary, and direction is a string
    :postcondition: checks if the direction is within the boundaries of the board and if it
                    is one of the four valid directions ('w', 'd', 'a', or 's')
    :return: True if the direction given is valid, False otherwise

    >>> my_board = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
    >>> my_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> validate_move(my_board, my_character, "w")
    False
    >>> validate_move(my_board, my_character, "5")
    False
    >>> validate_move(my_board, my_character, "s")
    True
    """
    target = next_position(character, direction)
    if not target:
        return False
    try:
        board[target]
    except KeyError:
        messages.validate_move_message(character, board, direction)
        return False
    else:
        return True


def check_if_goal_attained(bosses: tuple[dict[str, int | str | bool], ...]) -> bool:
    """
    Determine if main boss has been defeated.

    :param bosses: a list of dictionaries holding boss status information
    :precondition: each boss dictionary contains the key "alive"
    :postcondition: does not modify argument list
    :return: True if all bosses have alive == False, otherwise False

    >>> boss1 = {"name": "Boss1", "X-coordinate": 0, "Y-coordinate": 0, "alive": False, "Level_required": 1}
    >>> boss2 = {"name": "Amon, the God of Mischief",
    ... "X-coordinate": 1, "Y-coordinate": 1, "alive": False, "Level_required": 2}
    >>> check_if_goal_attained((boss1, boss2))
    True
    >>> boss1 = {"name": "Boss1", "X-coordinate": 0, "Y-coordinate": 0, "alive": True, "Level_required": 1}
    >>> boss2 = {"name": "Amon, the God of Mischief",
    ... "X-coordinate": 1, "Y-coordinate": 1, "alive": True, "Level_required": 2}
    >>> check_if_goal_attained((boss1, boss2))
    False
    """
    for boss in bosses:
        if boss["name"] == "Amon, the God of Mischief" and boss["alive"]:
            return False
    return True


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()