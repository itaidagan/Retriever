import json
import constants
from datetime import datetime
import sys
import psycopg2
import config


class RetrieverData:
    def __init__(self, json_string):
        parsed_dict = json.loads(json_string)
        if not all(key in parsed_dict for key in constants.REQUIRED_KEYS):
            missing_keys = list(filter(lambda x: x not in parsed_dict, constants.REQUIRED_KEYS))
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

        try:
            created_datetime = datetime.strptime(parsed_dict["created"], constants.DATETIME_FORMAT)
            self.created_date = created_datetime.strftime(constants.DATE_FORMAT)
            self.created_time = created_datetime.strftime(constants.TIME_FORMAT)
        except ValueError as e:
            print(f"Unable to parse 'created' timestamp, make sure format is {constants.DATETIME_FORMAT}")
            raise ValueError

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
            try:
                updated_datetime = datetime.strptime(parsed_dict["updated"], constants.DATETIME_FORMAT)
                updated_date = updated_datetime.strftime(constants.DATE_FORMAT)
                updated_time = updated_datetime.strftime(constants.TIME_FORMAT)
                return updated_date, updated_time
            except ValueError:
                print(f"Unable to parse 'updated' timestamp, make sure format is {constants.DATETIME_FORMAT}")
                raise ValueError
        return None, None

    def to_target_dict(self):
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

    def insert_to_db(self):
        self.to_target_dict()

        query = "INSERT INTO retriever(id, data) " \
                "VALUES(%s, %s);"
        conn = None
        try:
            conn = psycopg2.connect(
                host=config.HOST,
                database=config.DATABASE,
                user="postgres",
                password="admin")
            cur = conn.cursor()
            data = self.to_target_dict()
            data_as_json = json.dumps(data)
            cur.execute(query, (self.id, data_as_json))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Unable to insert to DB")
            print(error)
            raise error
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    item = RetrieverData(sys.argv[1])
    item.insert_to_db()
