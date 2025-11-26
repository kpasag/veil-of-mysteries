def move_character(character, direction):
    """
    Updates the player's position within the given direction.

    :param character: a dictionary containing the player's current coordinate and HP
    :param direction: a lowercase string representing the movement direction
                      ('n', 'e', 'w', or 's')
    :precondition: character is a dictionary and direction is a string
    :postcondition: modifies the character dictionary to reflect the new coordinates
                    based on the chosen direction

    >>> my_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> move_character(my_character, "n")
    >>> my_character["X-coordinate"]
    1
    >>> move_character(my_character, "e")
    >>> my_character["Y-coordinate"]
    3
    >>> move_character(my_character, "s")
    >>> my_character["X-coordinate"]
    2
    """
    if direction == "n":
        character["X-coordinate"] -= 1
    elif direction == "e":
        character["Y-coordinate"] += 1
    elif direction == "w":
        character["Y-coordinate"] -= 1
    else:
        character["X-coordinate"] += 1


def make_character():
    """
    Create a dictionary representing the player's position and health.

    :postcondition: create a character with a position of (0, 0) and 5 HP
    :return: a dictionary containing the player's position and current HP

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1}
