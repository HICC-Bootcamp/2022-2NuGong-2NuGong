# import Python's built-in JSON library
import json, sys
# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error

def json2sql(updateNotice):
    # use Python's open() function to load the JSON data
    # with open('test.json', encoding='utf-8') as json_data:

    #     # use load() rather than loads() for JSON files
    #     record_list = json.load(json_data)
    #     print("recordlst",record_list)
    first_record = updateNotice["sample"]
    # if type(record_list) == list:
    #     first_record = record_list[0]
    # get the column names from the first record
    columns = list(first_record[0].keys())
    print ("\ncolumn names:", columns)

    table_name = "rest_api_notice"
    sql_string = 'INSERT INTO {} '.format( table_name )
    sql_string += "(" + ', '.join(columns) + ")\nVALUES "
    print(sql_string)
    # enumerate over the record
    for i, record_dict in enumerate(first_record):

        # iterate over the values of each record dict object
        values = []
        for col_names, val in record_dict.items():

            # Postgres strings must be enclosed with single quotes
            if type(val) == str:
                # escape apostrophies with two single quotations
                val = val.replace("'", "''")
                val = "'" + val + "'"

            values += [ str(val) ]
            #한 공지당 [제목, 시간, 조회수, 본문]인 리스트 생성
            # join the list of values and enclose record in parenthesis
        sql_string += "(" + ', '.join(values) + "),\n"

    # remove the last comma and end statement with a semicolon
    sql_string = sql_string[:-2] + ";"
    print ("\nSQL statement:")
    print (sql_string)
    try:
        with open("backend\credentials.json", encoding='utf-8') as f:
            credentials = json.loads(f.read())
        # try:
            
        # except:
        #     print("credentials.json open failed")
        # declare a new PostgreSQL connection object
        conn = connect(
            dbname = credentials["DB_NAME"],
            user = credentials["DB_USER"],
            host = credentials["DB_HOST"],
            password = credentials["DB_PASSWORD"],
            # attempt to connect for 3 seconds then raise exception
            connect_timeout = 3
        )

        cur = conn.cursor()
        print ("\ncreated cursor object:", cur)

    except (Exception, Error) as err:
        print ("\npsycopg2 connect error:", err)
        conn = None
        cur = None
    # only attempt to execute SQL if cursor is valid
    if cur != None:

        try:
            cur.execute( sql_string )
            conn.commit()

            print ('\nfinished INSERT INTO execution')

        except (Exception, Error) as error:
            print("\nexecute_sql() error:", error)
            conn.rollback()

        # close the cursor and connection
        cur.close()
        conn.close()

