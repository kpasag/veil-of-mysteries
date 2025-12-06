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
    rows, columns = 10, 10
    board = game_board.make_board(rows, columns)
    character = player.make_character()
    bosses = combat.generate_bosses(board)
    achieved_goal = False
    messages.print_text_from_json("welcome_message")
    display_current_location(character, bosses, rows, columns)
    describe_current_location(board, character)
    while is_alive(character) and not achieved_goal:
        direction = messages.get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            player.move_character(character, direction)
            display_current_location(character, bosses, rows, columns)
            describe_current_location(board, character)
            for boss in bosses:
                if boss["X-coordinate"] == character["X-coordinate"] and \
                        boss["Y-coordinate"] == character["Y-coordinate"]:
                    combat.fight_boss(character, boss)
            if character["Level"] == 1:
                there_is_a_challenger = combat.check_for_foes()
                if there_is_a_challenger:
                    combat.check_player_level(character)
            achieved_goal = check_if_goal_attained(bosses)
    if is_alive(character) and achieved_goal:
        messages.print_text_from_json("win_message")
    if not is_alive(character):
        messages.print_text_from_json("lost_message")


def display_current_location(character, bosses, rows, columns):
    print("\nMap:")
    for row in range(rows):
        row_display = ""
        for column in range(columns):
            if (column, row) == (character["X-coordinate"], character["Y-coordinate"]):
                row_display += " P"
            elif any(boss["alive"] and boss["X-coordinate"] == column
                     and boss["Y-coordinate"] == row for boss in bosses):
                row_display += " B"
            else:
                row_display += " ."
        print(f" {row_display}")


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


def validate_move(board, character, direction):
    """
    Check whether the player's input for movement is valid.

    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param character: a dictionary containing the player's current coordinate and HP
    :param direction: a lowercase string representing the movement direction
                      ('w', 'd', 'a', or 's')
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
    x_position, y_position = character["X-coordinate"], character["Y-coordinate"]
    if direction == "w":
        target = (x_position, y_position - 1)
    elif direction == "s":
        target = (x_position, y_position + 1)
    elif direction == "a":
        target = (x_position - 1, y_position)
    elif direction == "d":
        target = (x_position + 1, y_position)
    else:
        return False
    try:
        board[target]
    except KeyError:
        return False
    else:
        return True


def check_if_goal_attained(bosses):
    """
    """
    for boss in bosses:
        if boss["name"] == "Amon, the God of Mischief" and boss["alive"]:
            return False
    return True


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