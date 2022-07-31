def findNoticeTag(noticeTitle):
    keywordlist = ["도서관", "고사", "전과", "장학", "동아리", "취업",
        "기숙사", "휴학·복학", "성적", "계절", "봉사", "프로그램"]
    isinlist = []
    parsingkeywordlist = ["도서관", "고사", "전과", "장학", "동아리", "채용", "취업",
        "기숙사", "휴학·복학", "성적", "계절", "봉사", "교육", "서포터즈", "프로그램"]
    
    for keyword in parsingkeywordlist:
        if keyword in noticeTitle:
            isinlist.append(1)
        else:
            isinlist.append(0)
    # for j in isinlist:
    #     print(j,end= " ")
    # 여기까지 가능한 형태 [000001000100001] 15개
    # 12개로 바꿔줘야함  5랑 6이랑 합쳐서 5, 12,13,14를 합쳐서 11으로 넣어주기
    isprogram = 0
    isemployee = 0
    isnewlist = []
    if (isinlist[12]+isinlist[13]+isinlist[14] ==0):
        isprogram = 0
    else:
        isprogram = 1
    if (isinlist[5]+isinlist[6] == 0):
        isemployee = 0
    else:
        isemployee = 1
    cnt = 0
    for j in range(len(parsingkeywordlist)):
        if(j==5):
            isnewlist.append(isemployee)
        elif (j==12):
            isnewlist.append(isprogram)
        elif (j==6)or(j==13)or(j==14):
            continue
        else:
            isnewlist.append(isinlist[j])
    
    flag = 0
    onehot_isinlist = []
    for i in isnewlist:
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

                return str(i+1) #태크번호 10~13 기타 는 13
    #print(17)
    #return "18"   

    
    
    
    
    
    
    # for k in onehot_isinlist:
    #     print(k, end=" ")
    # print("\n")
def main():
    print(findNoticeTag("기말프로그램 기간 중 일반열람실 운영 변경"))
    
main()