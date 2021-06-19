import json
from constants import REQUIRED_KEYS, DATETIME_FORMAT
from input import *
from datetime import datetime
import sys


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

        created_datetime = datetime.strptime(parsed_dict["created"], DATETIME_FORMAT)
        self.created_date = created_datetime.date()
        self.created_time = created_datetime.time()

        self.updated_date, self.updated_time = self.init_updated(parsed_dict)

        counters_dict = parsed_dict["counters"]
        if not all(key in counters_dict for key in ["score", "mistakes"]):
            print("score dictionary must contain both 'score' and 'mistakes' as keys")
            raise ValueError
        self.counters_total = int(counters_dict["score"]) + int(counters_dict["mistakes"])

    @staticmethod
    def init_items(parsed_dict):
        if "content" in parsed_dict and "marks" in parsed_dict["content"]:
            marks = parsed_dict["content"]["marks"]
            items = []
            for text_dict in marks:
                if "text" in text_dict:
                    items.append(text_dict["text"])
            return items
        else:
            return None

    @staticmethod
    def init_body(parsed_dict):
        if "content" in parsed_dict and "description" in parsed_dict["content"]:
            return parsed_dict["content"]["description"]
        else:
            return None

    # Assume that if updated is provided then it is in the same format as created
    # i.e. both date and time are provided
    @staticmethod
    def init_updated(parsed_dict):
        if "updated" in parsed_dict:
            updated_datetime = datetime.strptime(parsed_dict["updated"], DATETIME_FORMAT)
            return updated_datetime.date(), updated_datetime.time()
        return None, None

    def to_target_json(self):
        output_dict = dict()
        output_dict["path"] = self.path
        if self.items:
            output_dict["items"] = self.items
        if self.body:
            output_dict["body"] = self.body
        output_dict["id"] = self.id
        output_dict["author_name"] = self.author_name
        output_dict["author_id"] = self.author_id
        output_dict["created_date"] = self.created_date
        output_dict["created_time"] = self.created_time
        if self.updated_date:
            output_dict["updated_date"] = self.updated_date
            output_dict["updated_time"] = self.updated_time
        output_dict["counters_total"] = self.counters_total
        return output_dict


if __name__ == '__main__':
    # item = RetrieverData(GOOD_INPUT)
    # item2 = RetrieverData(MISSING_ADDRESS)
    # item3 = RetrieverData(MISSING_AUTHOR_ID)
    print(sys.argv[0])
    item = RetrieverData(sys.argv[1])
    print(item.to_target_json())
    # print(output)
