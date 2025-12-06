import json


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


def get_json():
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_list_of_message_from_json(key):
    json_data = get_json()
    return json_data[key]


def yield_text_from_json(key):
    json_data = get_json()
    for line in json_data[key]:
        yield colorize_text(line)


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
    combined_text = ""
    for line in json_data[key]:
        combined_text += colorize_text(line) + "\n"
    return combined_text.rstrip("\n")