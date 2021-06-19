import json
from constants import REQUIRED_KEYS
from input import *


class RetrieverData:
    def __init__(self, json_string):
        parsed_dict = json.loads(json_string)
        if not all(key in parsed_dict for key in REQUIRED_KEYS):
            raise ValueError

        author_dict = parsed_dict["author"]
        if not all (key in author_dict for key in ["username", "id"]):
            raise ValueError

        self.path = parsed_dict["address"]
        self.items = self.init_items(parsed_dict)
        self.body = self.init_body(parsed_dict)
        self.id = parsed_dict["id"]
        self.author_name = parsed_dict["author"]["username"]
        self.author_id = parsed_dict["author"]["id"]

    @staticmethod
    def init_items(parsed_dict):
        try:
            return parsed_dict["content"]["marks"]["text"]
        except:
            return None

    @staticmethod
    def init_body(parsed_dict):
        try:
            return parsed_dict["content"]["description"]
        except:
            return None


def parse_and_print_json(input_json):
    parsed_dict = json.loads(input_json)
    print(parsed_dict)
    for key, val in parsed_dict.items():
        print(f"The pair is {key}: {val}")


if __name__ == '__main__':
    item = RetrieverData(GOOD_INPUT)
