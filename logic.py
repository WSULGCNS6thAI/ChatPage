# 홍용민 11.14

print('우송대학교 챗봇 도우미입니다.')
print("건물 위치, 우송대 가는 길, 주요 시설을 알고 싶으면 '시설', 학과 및 학교 정보를 알고 싶으면 '학교'를 입력해주세요.")

a = input('원하시는 것을 입력해주세요. (시설 or 학교) : ')
if a == '시설':
    while True:
        b = input('건물 위치를 알고 싶으신가요? (yes or no) : ')
    
        if b == 'yes':
            c = input('위치를 찾을 건물을 입력해주세요 : ')
            # if c == 건물 이름들
            break
        elif b == 'no':
            d = input('우송대 가는길을 알고 싶으신가요? (yes or no) : ')
            if d == 'yes':
                e = input('출발지를 입력해주세요. (대전역 or 복합터미널) : ')
                if e == '대전역':
                    print('도보 5분 후 대전역/중앙시장에서 605번 버스 탑승, 자양동주민센터에서 하차 후 도보 5분')
                elif e == '복합터미널':
                    print('도보 4분 후 복합터미널에서 102번 버스 탑승, 우송대학교서캠퍼스에서 하차 후 도보 8분')
                break
            elif d == 'no':
                f = input('우송대학교 주요 시설에 대해 알고 싶으신가요? (yes or no) : ')
                if f == 'yes':
                    g = input('어느 시설에 대해 알고 싶으신가요? : ')
                    if g == '우송 도서관':
                        print('https://library.wsu.ac.kr')
                        print('대전광역시 동구 동대전로 171(자양동 155-3번지)')
                    elif g == '우송 유치원':
                        print('https://wsk.wsu.ac.kr')
                        print('대전광역시 동구 동대전로 171(자양동 155-3)우송유치원')
                    elif g == '사회 봉사단':
                        print('https://wusso.wsu.ac.kr/')
                        print('대전광역시 동구 동대전로 171 학생회관 (W16)3층')
                    elif g == '평생교육원':
                        print('https://llec.wsu.ac.kr:444/main/index.jsp')
                        print('대전광역시 동구 동대전로 171')
                    elif g == '우송비즈니스교육센터':
                        print('https://business.wsu.ac.kr:444/main/index.jsp')
                        print('대전광역시 동구 자양동 17-2번지 우송대학교 서캠퍼스 우송관 (W7) 4층 414호 비즈니스교육센터')
                    elif g == '우송IT교육센터':
                        print('https://itedu.wsu.ac.kr:444/page/index.jsp?code=itedu0104')
                        print('대전광역시 동구 백룡로 11번길 63 (자양동 52-2) 우송IT교육센터')
                    elif g == '외국어교육원':
                        print('http://wli.wsu.ac.kr/main/index.jsp#location')
                        print('대전광역시 동구 자양동 196-5번지 우송어학센터(S1)1층 외국어교육원')
                    elif g == '우송디젤철도아카데미':
                        print('https://railacademy.wsu.ac.kr:444/main/index.jsp')
                        print('대전광역시 동구 동대전로 171(자양동226-2) 서캠퍼스 철도물류관(W4) B107-4호')
                    elif g == '공자아카데미':
                        print('https://gongja.wsu.ac.kr:444/page/index.jsp?code=gongja0103')
                        print('대전광역시 동구 자양동 백룡로 5번길 66-1 우송어학센터 S1 공자아카데미 403호')
                    elif g == '한국어교육원':
                        print('http://wkli.wsu.ac.kr/story/page/index.jsp?code=wkli0105a')
                        print('대전광역시 동구 동대전로 171(자양동) 우송대학교 서캠퍼스 도서관 704호 우송한국어교육원')
                    else:
                        print('검색 결과가 없습니다.')
                    break
                if f == 'no':
                    print('찾으시는 정보가 없으므로 시설 정보 초기질문으로 돌아갑니다.')
                    
if a == '학교':
    def study_type():
        i = input('학과 관련 정보를 알고 싶으신가요? (yes or no) : ')
        if i == 'yes':
            while True:
                j = input('교육과정에 대해 알고 싶으신가요? (yes or no) : ')
                if j == 'yes':
                    k = input('원하시는 학과를 입력해주세요 : ')
                    # 해당 학과 교육과정
                    break
            
                elif j == 'no':
                    l = input('학과 설명을 듣고 싶으신가요? (yes or no) : ')
                    if l == 'yes':
                        m = input('원하시는 학과를 입력해주세요 : ')
                        # 해당 학과 설명
                        break
                    elif l == 'no':
                        print('찾으시는 정보가 없으므로 교육과정 초기질문으로 돌아갑니다.')

        elif i == 'no':
            o = input('학사 관련 정보를 알고 싶으신가요? (yes or no) : ')
            if o == 'yes':
                while True:
                    p = input('입학 관련 정보를 원하시나요? (yes or no) : ')
                    if p == 'yes':
                        # 입학 관련 서류 및 과정
                        break
                    elif p == 'no':
                        q = input('편입 관련 정보를 원하시나요? (yes or no) : ')
                        if q == 'yes':
                            # 편입 관련 서류 및 과정
                            break
                        elif q == 'no':
                            r = input('휴학 관련 정보를 원하시나요? (yes or no) : ')
                            if r == 'yes':
                                # 휴학 관련 서류 및 과정
                                break
                            elif r == 'no':
                                s = input('졸업 관련 정보를 원하시나요? (yes or no) : ')
                                if s == 'yes':
                                    # 졸업 관련 서류 및 과정
                                    break
                                elif s == 'no':
                                    print('찾으시는 정보가 없으므로 입학 초기질문으로 돌아갑니다.')
            elif o == 'no':
                print('찾으시는 정보가 없으므로 학과 초기질문으로 돌아갑니다.')
                study_type()
    study_type()
            # 학과, 학사로 roof or while
                
            
