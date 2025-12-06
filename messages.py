import json


def get_json():
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_text_from_json(json_data, key):
    lines = ""
    for line in json_data[key]:
        lines += line
    return lines


def yield_text_from_json(json_data, key):
    for line in json_data[key]:
        yield line


def print_text_from_json(json_data, key):
    for line in json_data[key]:
        print(line)


def colorize_text(text):
    colours = {"{PURPLE}": "\033[95m", "{RED}": "\033[91m", "{GREEN}": "\033[92m", "{YELLOW}": "\033[93m",
               "{BLUE}": "\033[94m", "{CYAN}": "\033[96m", "{GREY}": "\033[0m"}
    for key, value in colours.items():
        text = text.replace(key, value)
    return text


def get_full_text(json_data, key):
    combined_text = ""
    for line in json_data[key]:
        combined_text += colorize_text(line) + "\n"
    return combined_text.rstrip("\n")