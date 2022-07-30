from re import I
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
        record_list = json.loads(json_data.read())
        first_record = record_list["sample"] #list형태
         
    try: 
        cnt = 0
        for i in first_record:
            if(i["title"] == latest1):
                break
            else:
                cnt += 1
        newNotice = first_record[0:cnt+1]
        latest1 = first_record[0]["title"]
        if newNotice != []:
            #디비에 넣기
            update_notice_dict = dict()
            update_notice_dict["sample"] = []
            for i in newNotice:
                update_notice_dict["sample"].append(i)
            try:
                with open('test.json', 'w', encoding='utf-8') as file:
                    json.dump(update_notice_dict, file, ensure_ascii = False)
                    db.json2sql() #여기가 문제임.
                    print("젭알")
                print("잘 들어감")
            except:
                print("failure: couldn't dump data to database")
        # else: 쓰임이 없는 else문이라 주석처리함.
    except:
        print("Nothing new")
        latest1 = first_record[0]["title"]
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
while count<1:
    cr.chamsae_3('2', 2, 3)
    time.sleep(10)
    update_Detect()
    time.sleep(10)
    cr.chamsae_3('2', 1, 3)
    time.sleep(10)
    update_Detect()
    # schedule.run_pending()
    time.sleep(10)
    count += 1


