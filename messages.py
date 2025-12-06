import json
import time
from itertools import cycle
from typing import Generator


def get_user_choice() -> str:
    """
    Prompts the player for a direction to move.

    :postcondition: lower cases the players input and removes extra spaces in-between
    :return: the adjusting input as a string
    """
    type_text("\nWhich way will you go?\n"
              "'\033[96mW\033[0m' to go up, '\033[96mS\033[0m' to go down,"
              "'\033[96mD\033[0m' to go right, or '\033[96mA\033[0m' to go left.\n", 0.005)
    return input("Enter your choice: ").lower().strip()


def validate_move_message(character: dict[str, int], board: dict[tuple[int, int], str], direction: str) -> None:
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
    return {"Enzo_intro": cycle_text_from_json("Enzo_intro"),
            "Hvin_intro": cycle_text_from_json("Hvin_intro"),
            "Amon_intro": cycle_text_from_json("Amon_intro"),
            "boss_defeated": cycle_text_from_json("boss_defeated"),
            "player_lose_hp": cycle_text_from_json("player_lose_hp"),
            "victory_cycle": cycle_text_from_json("victory_cycle")}


def get_text_from_txt_file(file: str) -> list[str]:
    with open(file) as file_object:
        words = [line.strip() for line in file_object]
    return words


def get_json() -> dict[str, list[str]]:
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_list_of_message_from_json(key: str) -> list[str]:
    json_data = get_json()
    return json_data[key]


def cycle_text_from_json(key: str) -> Generator[str, None, None]:
    json_data = get_json()
    colored_lines = [colorize_text(line) for line in json_data[key]]
    yield from cycle(colored_lines)


def return_text_from_json(key: str) -> str:
    json_data = get_json()
    text = ""
    for line in json_data[key]:
        text += f"{colorize_text(line)}\n"
    return text


def colorize_text(text: str) -> str:
    colours = {"{PURPLE}": "\033[95m", "{RED}": "\033[91m", "{GREEN}": "\033[92m", "{YELLOW}": "\033[93m",
               "{BLUE}": "\033[94m", "{CYAN}": "\033[96m", "{GREY}": "\033[0m"}
    for key, value in colours.items():
        text = text.replace(key, value)
    return text


def get_full_text(key: str) -> str:
    json_data = get_json()
    return "\n".join(colorize_text(line) for line in json_data[key])


def type_text(text: str, delay: float = 0.03) -> None:
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()