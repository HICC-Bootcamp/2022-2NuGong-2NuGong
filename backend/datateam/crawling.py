from shutil import which
import requests
from bs4 import BeautifulSoup as bs
import json
import classificationFunc as classification
#대괄호 없애기 코드
import re

global department
global whichBoard
#각각의 공지 사이트와 첨부파일의 링크를 리스트에 정리하는 코드
def chamsae_1():
    global department
    global whichBoard
    print("게시판 메뉴")
    print("2 : 학교 일반 공지")
    print("3 : 학교 학생 공지")
    print("6 : 학교 행사/공모전 공지")
    print("54: 컴퓨터 공학과 공지")
    print("크롤링할 게시판을 선택하세요: ", end = "")
    whichBoard = input()
    if whichBoard == "2" or whichBoard == "3" or whichBoard == "6":
        department = "00"
    if whichBoard == "54":
        print("여기까지")
        department = "11"
    print("크롤링할 페이지의 범위를 입력하세요(예:1 3): ")
    page_start, page_end = map(int,input().split())
    lst_notice_link = []
    for i in range(page_start, page_end+1):
        url1 = "https://www.hongik.ac.kr/front/boardlist.do?currentPage="
        url2 = "&menuGubun=1&siteGubun=1&bbsConfigFK="
        url3 = "&searchField=ALL&searchValue=&searchLowItem=ALL"
        url = url1 + str(i) +url2 + whichBoard + url3
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        e = soup.find_all('a')

        for i in e:
            href = "https://www.hongik.ac.kr/"
            href += i.attrs['href']
            if("Download" in href):
                lst_notice_link[-1].append(href)
            else:
                lst_notice_link.append([href])
    return lst_notice_link
    



def chamsae_2():
    global department
    global whichBoard
    json_lst = []
    link_lst = chamsae_1()
    for i in link_lst:
        url = i[0]
        if(url == 'https://www.hongik.ac.kr/#'):
            continue
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        e = soup.find("span","text")
        try:
            title = e.text
        except:
            title = ""
        a = soup.find_all("span","value")

        try:
            when = a[1].text
        except:
            when = ""
        try:
            view_cnt = a[2].text
        except:
            view_cnt = ""
        b = soup.find_all("div","substance")
        try:
            title = (re.sub(r'\[[^)]*\]','',title))
            if whichBoard == "6": #행사및 공모전이면 태그 번호 17
                tag = "17"
            else:
                tag = classification.findNoticeTag(title)
            
            d = {"title" : title, "create_at" : when, "views" : view_cnt, "tag" : tag, "department" : department, "contents" : b[0].text}
            
            json_lst.append(d)
            """print(title, when, view_cnt, b[0].text)
            print('\n')"""
        except:
            continue
    return json_lst


def chamsae_3():
    file_path = "./test.json"

    
        
    json_lst = chamsae_2()
    json_dict = {}
    json_dict['sample'] = json_lst
    # json_dict["sample"].append(json_lst)
    print(json_dict)
    print("여기까지오키")
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file, ensure_ascii = False)
            
            #print(j)
        return 1
    except:
        return 0

if(chamsae_3() == 1):
    print("성공")
else:
    print("실패")
    
# def findNoticeTag(noticeTitle):
#     keywordlist = ["도서관", "고사", "전과", "장학", "동아리", "채용", "취업",
#         "기숙사", "휴학·복학", "성적", "계절", "봉사", "교육", "서포터즈", "프로그램"]
#     isinlist = []
#     for keyword in keywordlist:
#         if keyword in noticeTitle:
#             isinlist.append(1)
#         else:
#             isinlist.append(0)
#     # for j in isinlist:
#     #     print(j,end= " ")
#     # 여기까지 가능한 형태 [000001000100001]
#     flag = 0
#     onehot_isinlist = []
#     for i in isinlist:
#         if (i == 1) and (flag == 0):
#             flag += 1
#             onehot_isinlist.append(1)
#         elif (i == 1) and (flag == 1):
#             onehot_isinlist.append(0)
#         else:
#             onehot_isinlist.append(0)
#     # print("flag = ",flag,"\n")
#     if flag == 0:
#         onehot_isinlist.append(1)
#     else:
#         onehot_isinlist.append(0)
#         # 다 [000000000000000] 이면 기타로 분류 [0000000000000001]
#         # [str(universe),str(major),"전과","조교","기숙사","취업","채용","휴학.복학", "성적", "계절", "교육", "계절", "교육","서포터즈", "프로그램", "장학","봉사", "고사", "성적", "동아리", "도서관", "기타"]
#     for i, onehot in enumerate(onehot_isinlist):
#         if onehot == 1:
#             if i < 9:
#                 #print("0" + str(i+1))
#                 return "0" + str(i+1) # 태그번호 1~9까지는 앞에 0을 붙여줌
#             else:
#                 #print(str(i+1))
#                 return str(i+1) #태크번호 10~16
#     #print(17)
#     return "17" #태그 번호 17은 기타로 분류
    