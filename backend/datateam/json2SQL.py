# import Python's built-in JSON library
import json, sys

# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error
# use Python's open() function to load the JSON data
with open('test.json', encoding='utf-8') as json_data:

    # use load() rather than loads() for JSON files
    record_list = json.load(json_data)
first_record = record_list["sample"]
# if type(record_list) == list:
#     first_record = record_list[0]
# get the column names from the first record
columns = list(first_record[0].keys())
print ("\ncolumn names:", columns)

columns = [list(x.keys()) for x in record_list][0]