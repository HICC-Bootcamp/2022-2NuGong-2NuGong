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
        notice_update_dict = {}
        notice_update_dict["sample"] = newNotice
        print(notice_update_dict)
        # with open('test.json', 'w', encoding='utf-8') as file:
        #     json.dump(notice_update_dict, file, ensure_ascii = False)
        db.json2sql(notice_update_dict) #여기가 문제임.
        print("잘 들어감")
        # try:
            
        # except:
        #     print("failure: couldn't dump data to database")
    #    else: 쓰임이 없는 else문이라 주석처리함.     

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # except:
    #     print("Nothing new")
    #     latest1 = first_record[0]["title"]
    #     # latest1 = newNotice["title"]
    
    
    
# job2 = schedule.every(30).seconds.do(update_Detect)


job1 = schedule.every(30).seconds.do(cr.chamsae_3, '2', 2, 3)
job2 = schedule.every(30).seconds.do(update_Detect)
job3 = schedule.every(30).seconds.do(cr.chamsae_3, '2', 1, 3)
job4 = schedule.every(30).seconds.do(update_Detect)


count = 0
while True:
    schedule.run_pending()
    time.sleep(1)


