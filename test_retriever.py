import unittest
import retriever
import json


class TestRetriever(unittest.TestCase):

    def test_expected_output(self):
        test_input = '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": ' \
                     '"season"}, {"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
                     '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" :"68712648721648271"}, "id" : ' \
                     '"543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :1},' \
                     '"type" : "main"}'

        expected_output = '{"path": "https://www.google.com ", "items": ["marks", "season", "foo", "bar"], "body": ' \
                          '"Some description", "id": "543435435", "author_name": "Bob", "author_id": ' \
                          '"68712648721648271", "created_date": "2021-02-25", "created_time": "16:25:21+0000", ' \
                          '"updated_date": "2021-02-26", "updated_time": "08:21:20+0000", "counters_total": 4}'

        output_dict = retriever.RetrieverData(test_input).to_target_dict()
        self.assertEqual(json.dumps(output_dict), expected_output)

    def test_parsing_minimal_json(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        expected_output = '{"path": "https://www.google.com ", "id": "543435435", "author_name": "Bob", "author_id": ' \
                          '"68712648721648271", "created_date": "2021-02-25", "created_time": "16:25:21+0000", ' \
                          '"counters_total": 3}'
        output_dict = retriever.RetrieverData(test_input).to_target_dict()
        self.assertEqual(json.dumps(output_dict), expected_output)

    def test_json_parsing_error(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271", "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        self.assertRaises(json.decoder.JSONDecodeError, retriever.RetrieverData, test_input)

    def test_value_error_no_address(self):
        test_input = '{"addres" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_no_id(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "uuid" : "543435435","created" : "2021-02-25T16:25:21+00:00",' \
                     '"counters" : {"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_no_author_username(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"name" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_no_author_id(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob"}, "id" : "543435435",' \
                     '"created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_no_created(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_malformed_created_timestamp(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-0225T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_malformed_updated_timestamp(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","updated" : ' \
                     '"2021-02-2:21:20+00:00","counters" : {"score" : 3,"mistakes" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)

    def test_value_error_no_counters(self):
        test_input = '{"address" : "https://www.google.com ","author" : {"username" : "Bob","id" ' \
                     ':"68712648721648271"}, "id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : ' \
                     '{"score" : 3,"misses" :0}}'
        self.assertRaises(ValueError, retriever.RetrieverData, test_input)


if __name__ == '__main__':
    unittest.main()
