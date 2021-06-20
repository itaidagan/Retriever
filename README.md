#Retriever

##Requirements
1. Python
2. pip package psycopg2 (install using `pip install psycopg2`)
3. PostgreSQL server running locally or on an accessible machine. Default is localhost, change connection parameters in 
   config.py. Init the required table using `sql/create.sql`
   
## Usage
`python retriever.py <input json>`
See runme.sh for an example input. Remember to clear the database between runs (entries are unique)

## Testing
`python test_retriever.py`


## Documentation
See specification in "Python test assignment.pdf"
