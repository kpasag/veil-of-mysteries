def move_character(character: dict[str, int], direction: str) -> None:
    """
    Move the character one space in the given direction.


    :param character: a dictionary storing X and Y coordinates of the character
    :param direction: a lowercase string representing the movement direction
                      ('w', 'a', 's', or 'd)
    :precondition: character is a dictionary and direction is a string
    :postcondition: modifies the character dictionary to reflect the new coordinates
                    based on the chosen direction

    >>> my_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> move_character(my_character, "w")
    >>> my_character["X-coordinate"]
    2
    >>> move_character(my_character, "d")
    >>> my_character["Y-coordinate"]
    1
    >>> move_character(my_character, "s")
    >>> my_character["X-coordinate"]
    3
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
    Create a new character with starting stats.

    :postcondition: create a character starting at (0, 0) with HP=5 and Level=1
    :return: a dictionary containing the player's position and stats

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1}


def is_alive(character: dict[str, int]) -> bool:
    """
    Check whether the player is still alive based on their current HP.

    :param character: a dictionary containing the player's current coordinate and HP
    :precondition: character is a string
    :postcondition: determine if the player is still alive or not based on their HP
    :return: True if the player HP is greater than 0, False otherwise

    >>> my_character = {"Current HP": 5}
    >>> is_alive(my_character)
    True
    >>> my_character["Current HP"] = 0
    >>> is_alive(my_character)
    False
    """
    return character["Current HP"] != 0