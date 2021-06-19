'''
1. Parse string
2. Check that all necessary values are present
3. Throw error if not
4. Insert into new format
5. Push to DB
    a. Establish connection
    b. Insert data
    c. Verify


Optimize if needed
'''

SAMPLE_INPUT = '{"address" : "https://www.google.com ","content" : {"marks" : [{"text": "marks"},{"text": "season"},' \
               '{"text": "foo"},{"text":"bar"}],"description" : "Some description"},"updated" : ' \
               '"2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" :"68712648721648271"},' \
               '"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"score" : 3,"mistakes" :0},' \
               '"type" : "main"} '

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')
