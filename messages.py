import json
from itertools import cycle


def get_user_choice():
    """
    Prompts the player for a direction to move.

    :postcondition: lower cases the players input and removes extra spaces in-between
    :return: the adjusting input as a string
    """
    return input("Which way will you go?\n"
                 "'\033[96mW\033[0m' to go up, '\033[96mS\033[0m' to go down,"
                 "'\033[96mD\033[0m' to go right, or '\033[96mA\033[0m' to go left.\n"
                 "Enter your choice: ").lower().strip()


def validate_move_message(character, board, direction):
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


def get_text_from_txt_file(file):
    with open(file) as file_object:
        words = [line.strip() for line in file_object]
    return words


def get_json():
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_list_of_message_from_json(key):
    json_data = get_json()
    return json_data[key]


def cycle_text_from_json(key):
    json_data = get_json()
    colored_lines = [colorize_text(line) for line in json_data[key]]
    return cycle(colored_lines)

def print_text_from_json(key):
    json_data = get_json()
    for line in json_data[key]:
        print(colorize_text(line))


def colorize_text(text):
    colours = {"{PURPLE}": "\033[95m", "{RED}": "\033[91m", "{GREEN}": "\033[92m", "{YELLOW}": "\033[93m",
               "{BLUE}": "\033[94m", "{CYAN}": "\033[96m", "{GREY}": "\033[0m"}
    for key, value in colours.items():
        text = text.replace(key, value)
    return text


def get_full_text(key):
    json_data = get_json()
    return "\n".join(colorize_text(line) for line in json_data[key])
