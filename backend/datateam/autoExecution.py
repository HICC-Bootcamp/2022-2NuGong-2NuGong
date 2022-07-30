import schedule
import time
import json
import crawling as cr
import json2SQL as db
global latest1
latest1 = ""
# job1 = schedule.every(30).seconds.do(cr.chamsae_3, '2', 1, 1)
def update_Detect():
    global latest1
    with open('test.json', encoding='utf-8') as json_data:
        # use load() rather than loads() for JSON files
        record_list = json.load(json_data)
        first_record = record_list["sample"] #list형태
        
        print("바바보")
    try: 
        
        newNotice = first_record[0:first_record.find(latest1)]
        latest1 = first_record[0]["title"]
        if newNotice != []:
            #디비에 넣기
            try:
                with open('test.json', 'w', encoding='utf-8') as file:
                    for i in newNotice:
                        json.dump(i, file, ensure_ascii = False)
                        db.json2sql()
                print("잘 들어감")
            except:
                print("실패")
        else:
            
            print("바보")
    except:
        print("업데이트안댐")
        # newNotice = first_record[0]
        # latest1 = newNotice["title"]
        
    
    
# job2 = schedule.every(30).seconds.do(update_Detect)


job1 = schedule.every(30).seconds.do(cr.chamsae_3, '2', 2, 3)
job2 = schedule.every(30).seconds.do(update_Detect)
job3 = schedule.every(30).seconds.do(cr.chamsae_3, '2', 1, 3)
job4 = schedule.every(30).seconds.do(update_Detect)
# job3 = time.sleep(10)
# job4 = schedule.every(60).seconds.do(cr.chamsae_3, '3', 1, 1)
# job5 = db.json2sql()
# job6 = time.sleep(10)
# job7 = schedule.every(60).seconds.do(cr.chamsae_3, '6', 1, 1)
# job8 = db.json2sql()
# job9 = time.sleep(10)
# job10 = schedule.every(60).seconds.do(cr.chamsae_3, '54', 1, 1)
# job11 = db.json2sql()

# job12 = time.sleep(10)
# # 1분에 한번씩 함수 실행

count = 0
while True:
    schedule.run_pending()
    time.sleep(1)