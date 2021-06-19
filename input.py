GOOD_INPUT = '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},' \
             '{"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
             '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" :"68712648721648271"},' \
             '"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :0},' \
             '"type" : "main"}'

MISSING_ADDRESS = '{"addrekk" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},' \
             '{"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
             '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" :"68712648721648271"},' \
             '"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :0},' \
             '"type" : "main"}'

MISSING_AUTHOR_ID = '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},' \
             '{"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
             '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","i" :"68712648721648271"},' \
             '"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :0},' \
             '"type" : "main"}'

MISSING_SCORES = '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},' \
             '{"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
             '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","i" :"68712648721648271"},' \
             '"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"mistakes" :0},' \
             '"type" : "main"}'