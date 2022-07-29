from psycopg2 import connect, Error



def quiz(input_id):
    #조회수리스트받기
    #viewlist = sql.favorite(id)
    try:
        conn = connect(
        dbname = "zahzrhge",
        user = "zahzrhge",
        host = "arjuna.db.elephantsql.com",
        password = "메롱",
        # attempt to connect for 3 seconds then raise exception
        connect_timeout = 3
    )

        cur = conn.cursor()
        print ("\ncreated cursor object:", cur)
    
    except (Exception, Error) as err:
        print ("\npsycopg2 connect error:", err)
        conn = None
        cur = None
    if cur != None:

        try:
            sql_string = 'SELECT favorites from public.rest_api_user where id = {}'.format(input_id)
            cur.execute(sql_string)
            
            result = cur.fetchone();#Fetching 1st row from the table
            print(result)
            
            print ('\nfinished SELECT favorites execution')
            
        except (Exception, Error) as error:
            print("\nexecute_sql() error:", error)
            
    taglist = list()
    viewlist = list(result)[0]
    tmp1 = max(viewlist)    
    index1 = viewlist.index(tmp1)
    viewlist[index1] = -1
    tmp2 = max(viewlist)
    index2 = viewlist.index(tmp2)
    viewlist[index2] = -1
    tmp3 = max(viewlist)
    index3 = viewlist.index(tmp3)
    viewlist[index3] = -1
    if tmp1 != 0:
        taglist.append(index1)
    if tmp2 != 0:
        taglist.append(index2)
    if tmp3 != 0:
        taglist.append(index3)    
    print(taglist)
    
    cur.close()
    conn.close()

def main():
    quiz(20)
main()