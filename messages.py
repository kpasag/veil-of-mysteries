"""
Kyle Pasag
A01428389

Module for handling in-game text and dialogue management.

This module loads and formats text from external files, including both JSON
and plain text resources. It provides functions for retrieving messages,
cycling dialogue lines, replacing color tokens with ANSI codes, and typing
animated text to the console, all of which support narrative and visual
feedback in the game.
"""
import json
import time
from itertools import cycle
from typing import Generator


def get_user_choice() -> str:
    """
    Prompts the player for a direction to move.

    :postcondition: lower cases the players input and removes extra spaces in-between
    :return: the adjusted input as a string
    """
    type_text("\nWhich way will you go?\n"
              "'\033[96mW\033[0m' to go up, '\033[96mS\033[0m' to go down,"
              "'\033[96mD\033[0m' to go right, or '\033[96mA\033[0m' to go left.\n", 0.005)
    return input("Enter your choice: ").lower().strip()


def validate_move_message(character: dict[str, int], board: dict[tuple[int, int], str], direction: str) -> None:
    """
    Display a message if the user attempts to move in an invalid direction.

    :param character: a dictionary storing X and Y coordinates of the character
    :param board: a dictionary representing the game board, where keys are a row and a column
                  that represent a coordinate and the value is the room description
    :param direction: a lowercase string representing the movement direction
                      ('w', 'a', 's', or 'd)
    :precondition: character and board are a dictionary and direction is a string
    :postcondition: check if direction is valid and print a response
    """
    x_position, y_position = character["X-coordinate"], character["Y-coordinate"]
    max_row = max(coordinate[0] for coordinate in board.keys())
    max_col = max(coordinate[1] for coordinate in board.keys())
    if direction == "w" and y_position == 0:
        print("You can't go further north.")
    elif direction == "s" and y_position == max_col:
        print("You can't go further east.")
    elif direction == "a" and x_position == 0:
        print("You can't go further west.")
    elif direction == "d" and x_position == max_row:
        print("You can't go further south.")
    else:
        print("Please try again.")


def generate_dialogue() -> dict[str, Generator[str, None, None]]:
    """
    Create a mapping of dialogue category names to cycling text generators.

    :precondition: messages.json must be present and correctly formatted
    :postcondition: returns a dictionary where each value cycles through themed text lines
    :return: dictionary mapping dialogue names to generators that yield colored strings
    """
    return {"Enzo_intro": cycle_text_from_json("Enzo_intro"),
            "Hvin_intro": cycle_text_from_json("Hvin_intro"),
            "Amon_intro": cycle_text_from_json("Amon_intro"),
            "boss_defeated": cycle_text_from_json("boss_defeated"),
            "player_lose_hp": cycle_text_from_json("player_lose_hp"),
            "victory_cycle": cycle_text_from_json("victory_cycle")}


def get_text_from_txt_file(file: str) -> list[str]:
    """
    Read a list of lines from a text file.

    :param file: a string representing the file name to read
    :precondition: file must exist and be a valid text file
    :postcondition: strip every line and store it in a list
    :return: the list containing the file strings
    """
    with open(file) as file_object:
        words = [line.strip() for line in file_object]
    return words


def get_json() -> dict[str, list[str]]:
    """
    Load and return JSON data from the messages json file.

    :precondition: messages.json file must exist and contain valid JSON
    :postcondition: returns a dictionary loaded from the JSON file
    :return: a dictionary of message lists
    """
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_list_of_message_from_json(key: str) -> list[str]:
    """
    Retrieve a list of message strings by key from JSON.

    :param key: a string representing the key name in the json file
    :precondition: key is a string and exists in the json file
    :postcondition: get the list from the json file
    :return: the list from the json file
    """
    json_data = get_json()
    return json_data[key]


def cycle_text_from_json(key: str) -> Generator[str, None, None]:
    """
    Yield an infinite cycle of colored message lines from JSON.

    :param key: a string representing the key name in the json file
    :precondition: key is a string and exists in the json file
    :postcondition: creates an endless generator cycling formatted text
    :return: generator that yields colored lines of text forever
    """
    json_data = get_json()
    colored_lines = [colorize_text(line) for line in json_data[key]]
    yield from cycle(colored_lines)


def return_text_from_json(key: str) -> str:
    """
    Create a single formatted string by joining all lines of a message block.

    :param key: a string representing the key name in the json file
    :precondition: key is a string and exists in the json file
    :postcondition: produces a newline-separated formatted message block
    :return: the colored and newline-joined string
    """
    json_data = get_json()
    text = ""
    for line in json_data[key]:
        text += f"{colorize_text(line)}\n"
    return text


def colorize_text(text: str) -> str:
    """
    Convert formatting tokens into terminal ANSI color codes.

    :param text: string that may contain color tokens like {RED} or {CYAN}
    :precondition: text must be a string
    :postcondition: converts the tokens inside the string into ANSI color codes
    :return: colored string
    """
    colours = {"{PURPLE}": "\033[95m", "{RED}": "\033[91m", "{GREEN}": "\033[92m", "{YELLOW}": "\033[93m",
               "{BLUE}": "\033[94m", "{CYAN}": "\033[96m", "{GREY}": "\033[0m"}
    for key, value in colours.items():
        text = text.replace(key, value)
    return text


def get_full_text(key: str) -> str:
    """
    Return a colored multi-line block of text for a JSON key.

    :param key: a string representing the key name in the json file
    :precondition: key is a string and exists in the json file
    :postcondition: converts the list of strings into one full string
    :return: the converted string
    """
    json_data = get_json()
    return "\n".join(colorize_text(line) for line in json_data[key])


def type_text(text: str, delay: float = 0.03) -> None:
    """
    Print the given text character-by-character with a delay.

    :param text: full string to type out
    :param delay: per-character delay in seconds
    :precondition: text is a string, delay is a non-negative float
    :postcondition: displays text with typing animation effect
    """
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()