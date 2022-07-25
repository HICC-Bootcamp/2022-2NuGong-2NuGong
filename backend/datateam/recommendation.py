# score = 0 info[id][major]
# noticeinfo = {"게시물번호": {"키워드": "시험", 작성자, 작성날짜 }}
# info = {아이디: {정보 담은 딕셔너리}}
# info = [{id: {"major": 11, "univname": 0(공과), "inter_keyword1":0 ,"inter_keyword2" ,inter_keyword3 , uninter_keyword1 ,uninter_keyword2 ,uninter_keyword3}} ]
# def majordistance(user.id, another.id):
# 		if (info[user.id][major] != info[another.id][major]) and (단과대학 다르면 ): 
# 				return 0
# 		else if (info[user.id][major] != info[another.id][major]) and (단과대학 같으면 ): 
# 				return 2
# 		else:
# 				return 4
# [키워드 리스트 끼리 비교해야 할듯]
# def keyworddistance(user.keyword, another.keyword):
# 	다르면 1, 키워드 같으면 0반환
# def interkeywordSimilar2(user.interkeyword, another.interkeyword)
# 	관심 키워드 다르면 0, 관심 키워드 같으면 1반환	
# def majorSimilar(user.major, another.major)
# def majorSimilar(user.major, another.major)
# def majorSimilar(user.major, another.major)

# 루트(4+1+1+0+0+1+0+0) => 학과같고 키워드 같을 수록 크기가 작아지도록 ? 

# 관심키워드랑, 전공설정되어있으면 그냥 그룹으로 묶어놓으면 될듯..? 
# 8*(2**16) = 2**19 
# sort해서 (열번째(첫번째사람대신)사람이 본 공지 - user가 본 공지)를 추천해준다.

# #수도코드짜자
# 전공별 조회수 쌓인다
# 조건 : 그 게시물 날짜와 현재 날짜 차이 7일 이내
# 조회수 딕셔너리 = {”컴퓨터공학과”: 35, “산업공학과”: 68,...... }
# 학과별 조회수 threshold 딕셔너리 = {"컴퓨터공학과":[전공 == 컴공인 사람수]* 0.3 , “산업공학과”: [이누공 가입 and 전공 == 산공 사람수]* 0.3,...... }
# #threshold의 업데이트는 사용자수 변화시 즉각적으로 가능한가?
# 가입할때마다 업데이트 해준다.
# 학과별 조회수 > threshold 인 학과 이용자들에게 추천해준다.
# EX. threshold = 학과별 앱 가입한 이용자들의 수 * 0.3


#학과 인기글
#현재 추천하는 공지를 어떤 기준으로 정할 것인지를 정해야함.
#변경된 조회수에의한 추천공지리스트 변경은 1시간마다 실시

#TODO usersmajor = database에서 받아온 major에 해당하는 번호
usersmajor = 11
#{"컴퓨터공학과": 50, "자율전공학부": 80} 이누공 가입자수 
#{"컴퓨터공학과": 35, "자율전공학부": 68} 각 공지에 따른 조회수
signnum = {"11": 50, "35": 80}
recentNotices = [134, 135, 136]
recommendNotice = list() #추천 공지 리스트
for recentNotice in recentNotices: #  /근 7일간의 새로운 공지가 떴어
	recentNotice.views  # {"11": 35, "35": 68} .views 메소드 있을거라는 상상
	for i in recentNotice.views.keys():
		if usersmajor == i:
			thisview = recentNotice.views[i] #내 학과 사람들이 얼마나 읽었는지
			break
	if signnum[usersmajor]*0.3 < thisview:
		recommendNotice.append(recentNotice)
    	#공지를 추천한다.
	else:
		continue
		#추천 안함.
