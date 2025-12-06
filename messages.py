import json


def get_json():
    with open('messages.json', 'r', encoding="utf-8") as data:
        return json.load(data)


def get_text_from_json(json_data, text):
    lines = ""
    for line in json_data[text]:
        lines += line
    return lines


def yield_text_from_json(json_data, text):
    for line in json_data[text]:
        yield line


def print_text_from_json(json_data, text):
    for line in json_data[text]:
        print(line)



def colorize_text(text):
    colours = {"{PURPLE}": "\033[95m", "{RED}": "\033[91m", "{GREEN}": "\033[92m", "{YELLOW}": "\033[93m",
               "{BLUE}": "\033[94m", "{CYAN}": "\033[96m", "{GREY}": "\033[0m"}
    for key, value in colours.items():
        text = text.replace(key, value)
    return text