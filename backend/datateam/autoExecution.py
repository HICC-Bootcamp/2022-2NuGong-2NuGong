import schedule
import time
import json
import crawling as cr
import json2SQL as db
#"교내 모든 전산 서비스 중단 안내", "2022학년도 제2학기 대학(원) 재학생 등록금 납부 안내", "온라인 브레인스토밍‘재밍(Jamming)’홍보", "창직프로젝트1,2 수강신청 관련 공지 (제출기한 : ~8/8)"
latest1, latest2, latest3, latest4 = "교내 모든 전산 서비스 중단 안내", "2022학년도 제2학기 대학(원) 재학생 등록금 납부 안내", "온라인 브레인스토밍‘재밍(Jamming)’홍보", "창직프로젝트1,2 수강신청 관련 공지 (제출기한 : ~8/8)"
list1 = [latest1]
list2 = [latest2]
list3 = [latest3]
list4 = [latest4]

def update_Detect(lst):
    try:
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
    except:
        print("failure: couldn't open data from json file")
   

job1 = schedule.every(1).seconds.do(cr.chamsae_3, '2', 1, 10)
job2 = schedule.every(1).seconds.do(update_Detect, list1)
job3 = schedule.every(1).seconds.do(cr.chamsae_3, '3', 1, 10)
job4 = schedule.every(1).seconds.do(update_Detect, list2)
job5 = schedule.every(1).seconds.do(cr.chamsae_3, '6', 1, 10)
job6 = schedule.every(1).seconds.do(update_Detect, list3)
job7 = schedule.every(1).seconds.do(cr.chamsae_3, '54', 1, 10)
job8 = schedule.every(1).seconds.do(update_Detect, list4)

while True:
    schedule.run_pending()
    time.sleep(2)


