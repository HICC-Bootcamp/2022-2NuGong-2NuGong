
# TODO [sentence는 BE TEAM이 크롤링한 데이터 서버에다가 저장해놓으면 끌어오는 코드로 변경해야함.]
# 공지 제목이 리스트로 주어져있을때, 공지를 keywordlist에서 해당하는 키워드 하나만 원핫인코딩 리스트 반환하는 공지 분류 코드 작성 완료
# 공지 제목 크롤링 받은거[리스트에 저장]
# TODO [noticeList는 BE TEAM이 일반공지, 학생공지, 기숙사 공지에서 크롤링한 공지 제목 데이터를 서버에다가 저장해놓으면 갖고 오는 코드로 변경해야함.]
noticeList = ['하계방학 중 중앙 운영 조정 안내', '기말고사 기간 중 일반열람실 운영 변경', '4차 산업혁명 교육체계 구축 지원 프로그램 시행',
              '정보전산원 공용PC실 봉사장학생(대학원생) 모집 안내', '기업체 취업/창업/인턴 상담 및 지도 프로그램 안내', '2021학년도 동계계절학기 성적조회 안내(바이오헬스 과목 성적조회 포함)']

for sentence in noticeList:
    keywordlist = ["도서관", "고사", "전과", "장학", "동아리", "채용", "취업",
                   "기숙사", "휴학·복학", "성적", "계절", "봉사", "교육", "서포터즈", "프로그램"]
    isinlist = []
    for keyword in keywordlist:
        if keyword in sentence:
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
    for k in onehot_isinlist:
        print(k, end=" ")
    print("\n")
