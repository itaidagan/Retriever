import json
from constants import REQUIRED_KEYS, DATETIME_FORMAT
from input import *
from datetime import datetime


class RetrieverData:
    def __init__(self, json_string):
        parsed_dict = json.loads(json_string)
        if not all(key in parsed_dict for key in REQUIRED_KEYS):
            missing_keys = list(filter(lambda x: x not in parsed_dict, REQUIRED_KEYS))
            print("The following keys must be present in input json")
            print(missing_keys)
            raise ValueError

        self.path = parsed_dict["address"]
        self.items = self.init_items(parsed_dict)
        self.body = self.init_body(parsed_dict)
        self.id = parsed_dict["id"]

        author_dict = parsed_dict["author"]
        if not all(key in author_dict for key in ["username", "id"]):
            print("author dictionary must contain both 'username' and 'id' as keys")
            raise ValueError
        self.author_name = parsed_dict["author"]["username"]
        self.author_id = parsed_dict["author"]["id"]

        created = datetime.strptime(parsed_dict["created"], DATETIME_FORMAT)
        self.created_date = created.date()
        self.created_time = created.time()

        if "updated" in parsed_dict:
            self.updated = datetime.strptime(parsed_dict["updated"], DATETIME_FORMAT)
        else:
            self.updated = None

        counters_dict = parsed_dict["counters"]
        if not all(key in counters_dict for key in ["score", "mistakes"]):
            raise ValueError
        self.counters_total = int(counters_dict["score"]) + int(counters_dict["mistakes"])

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


if __name__ == '__main__':
    # item = RetrieverData(GOOD_INPUT)
    # item2 = RetrieverData(MISSING_ADDRESS)
    item3 = RetrieverData(MISSING_AUTHOR_ID)
