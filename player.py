def move_character(character: dict[str, int], direction: str) -> None:
    """
    Updates the player's position within the given direction.

    :param character: a dictionary containing the player's current coordinate and HP
    :param direction: a lowercase string representing the movement direction
                      ('n', 'e', 'w', or 's')
    :precondition: character is a dictionary and direction is a string
    :postcondition: modifies the character dictionary to reflect the new coordinates
                    based on the chosen direction

    >>> my_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> move_character(my_character, "W")
    >>> my_character["X-coordinate"]
    1
    >>> move_character(my_character, "D")
    >>> my_character["Y-coordinate"]
    3
    >>> move_character(my_character, "s")
    >>> my_character["X-coordinate"]
    2
    """
    if direction == "w":
        character["Y-coordinate"] -= 1
    elif direction == "s":
        character["Y-coordinate"] += 1
    elif direction == "a":
        character["X-coordinate"] -= 1
    elif direction == "d":
        character["X-coordinate"] += 1


def make_character() -> dict[str, int]:
    """
    Create a dictionary representing the player's position and health.

    :postcondition: create a character with a position of (0, 0) and 5 HP
    :return: a dictionary containing the player's position and current HP

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1}


def is_alive(character: dict[str, int]) -> bool:
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