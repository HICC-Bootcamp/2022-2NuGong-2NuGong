def findNoticeTag(noticeTitle):
    keywordlist = ["도서관", "고사", "전과", "장학", "동아리", "채용", "취업",
        "기숙사", "휴학·복학", "성적", "계절", "봉사", "교육", "서포터즈", "프로그램"]
    isinlist = []
    for keyword in keywordlist:
        if keyword in noticeTitle:
            isinlist.append(1)
        else:
            isinlist.append(0)
    # for j in isinlist:
    #     print(j,end= " ")
    # 여기까지 가능한 형태 [000001000100001]
    flag = 0
    onehot_isinlist = []
    for i in isinlist:
        if (i == 1) and (flag == 0):
            flag += 1
            onehot_isinlist.append(1)
        elif (i == 1) and (flag == 1):
            onehot_isinlist.append(0)
        else:
            onehot_isinlist.append(0)
    # print("flag = ",flag,"\n")
    if flag == 0:
        onehot_isinlist.append(1)
    else:
        onehot_isinlist.append(0)
        # 다 [000000000000000] 이면 기타로 분류 [0000000000000001]
        # [str(universe),str(major),"전과","조교","기숙사","취업","채용","휴학.복학", "성적", "계절", "교육", "계절", "교육","서포터즈", "프로그램", "장학","봉사", "고사", "성적", "동아리", "도서관", "기타"]
    for i, onehot in enumerate(onehot_isinlist):
        if onehot == 1:
            if i < 9:
                #print("0" + str(i+1))
                return "0" + str(i+1) # 태그번호 1~9까지는 앞에 0을 붙여줌
            else:
                #print(str(i+1))

                return str(i+1) #태크번호 10~16 기타 는 16
    #print(17)
    #return "18"   

    
    
    
    
    
    
    # for k in onehot_isinlist:
    #     print(k, end=" ")
    # print("\n")
def main():
    print(findNoticeTag("기말고사 기간 중 일반열람실 운영 변경"))
    
main()