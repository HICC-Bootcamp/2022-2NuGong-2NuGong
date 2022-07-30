from re import I
import schedule
import time
import json
import crawling as cr
import json2SQL as db
latest1, latest2, latest3, latest4 = "세종캠퍼스 산업스포츠학과 조교 모집", "2022학년도 제2학기 국가근로 및 교내봉사 장학생 선발안내", "2022년도 중성자 회절 여름학교 안내", "2022학년도 전공별 졸업생 취업특강 및 직업탐방 세미나 참여신청 안내(서울캠퍼스) (~01.06)"
list1 = [latest1]
list2 = [latest2]
list3 = [latest3]
list4 = [latest4]

def update_Detect(lst):
    with open('test.json', encoding='utf-8') as json_data:
        # use load() rather than loads() for JSON files
        record_list = json.loads(json_data.read())
        first_record = record_list["sample"] #list형태
    cnt = 0
    for i in first_record:
        if(i["title"] == lst[0]):
            break
        else:
            cnt += 1
    newNotice = first_record[0:cnt]
    lst[0] = first_record[0]["title"]
    if newNotice != []:
        #디비에 넣기
        notice_update_dict = {}
        notice_update_dict["sample"] = newNotice
        #print(notice_update_dict)
        db.json2sql(notice_update_dict) #여기가 문제임.
        print("잘 들어감")
        # except:
        #     print("failure: couldn't dump data to database")
    #    else: 쓰임이 없는 else문이라 주석처리함.     
    # except:
    #     print("Nothing new")
    #     latest1 = first_record[0]["title"]
    #     # latest1 = newNotice["title"]
        
    
    

job1 = schedule.every(1).seconds.do(cr.chamsae_3, '2', 1, 1)
job2 = schedule.every(1).seconds.do(update_Detect, list1)
job3 = schedule.every(1).seconds.do(cr.chamsae_3, '3', 1, 1)
job4 = schedule.every(1).seconds.do(update_Detect, list2)
job5 = schedule.every(1).seconds.do(cr.chamsae_3, '6', 1, 1)
job6 = schedule.every(1).seconds.do(update_Detect, list3)
job7 = schedule.every(1).seconds.do(cr.chamsae_3, '54', 1, 1)
job8 = schedule.every(1).seconds.do(update_Detect, list4)

while True:
    schedule.run_pending()
    time.sleep(2)


