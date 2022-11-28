# 22.11.21 김경호
from konlpy.tag import Komoran

komoran = Komoran(userdic='dataset/dic.user')

def logic1(userInput):
    nouns = komoran.nouns(userInput)
    #level1.id = 2
    if '시설' in nouns:
        return 2
    
    #level1.id = 1
    elif '학교' in nouns:
        return 1
#11-21 조영수 level 2,3추가
def logic2(userInput):
    nouns = komoran.nouns(userInput)
    #level2.id 
    if '학과' in nouns:
        return 1
    elif '학사' in nouns:
        return 2
    elif '건물' in nouns or '위치' in nouns:
        return 3
    elif '대중교통' in nouns:
        return 4
    elif '주요시설' in nouns:
        return 5
    #level3.id 
def logic3(userInput):
    nouns = komoran.nouns(userInput)
    if '휴학' in nouns:
        return 1
    elif '전과' in nouns:
        return 2
    elif '입학' in nouns:
        return 3
    elif '자퇴/제적' in nouns:
        return 4
    elif '졸업' in nouns:
        return 5
    elif '복합터미널' in nouns or '복터' in nouns or '복합' in nouns or '터미널'in nouns:
        return 6
    elif '대전역' in nouns:
        return 7
    elif '도서관' in nouns or'우송도서관' in nouns:
        return 8
    elif '유치원' in nouns or '우송유치원'in nouns:
        return 9
    elif '사회봉사단' in nouns or '사회' in nouns or '봉사단' in nouns:
        return 10    
    elif '평생교육원' in nouns or '평생' in nouns:
        return 11
    elif '우송비즈니스 교육센터' in nouns or '비즈니스 교육센터' in nouns or '비즈니스' in nouns:
        return 12
    elif '우송 IT교육센터' in nouns or 'IT교육센터' in nouns  in nouns:
        return 13
    elif '외국어교육원' in nouns or '외국어' in nouns:
        return 14
    elif '우송디젯철도 아카데미' in nouns or '디젯철도 아카데미' in nouns or '디젯철도'  in nouns:
        return 15
    elif '공자아카데미' in nouns or '우송공자아카데미' in nouns  or '공자'  in nouns:
        return 16
    elif '한국어교육원' in nouns or '국어교육' in nouns or '원' in nouns:
        return 17
    elif '우송예술회관' in nouns or '예술회관' in nouns or '예술' in nouns or '회관' in nouns:
        return 18
    elif '우송수련원' in nouns or '수련원' in nouns:
        return 19
    elif '우송스포츠센터' in nouns or '스포츠센터' in nouns or '센터' in nouns:
        return 20
    elif 'F스포렉스' in nouns or '스포렉스' in nouns or '스포' in nouns or '렉스' in nouns:
        return 21
    elif '대전화병원' in nouns or '화병원' in nouns or '전화' in nouns or '병원' in nouns:
        return 22
    elif '컴퓨터정보보안' in nouns or '컴정' in nouns or '컴퓨터' in nouns or '정보' in nouns or '보안' in nouns:
        return 23
    elif 'AI빅데이터' in nouns or 'AI' in nouns or '빅' in nouns or '데이터' in nouns:
        return 24
    elif '글로벌호텔매니지먼트' in nouns or '글호' in nouns  or '호텔' in nouns or '매니지먼트' in nouns:
        return 25
    elif '글로벌융합비즈니스' in nouns or '글비' in nouns or '융합' in nouns or '비즈니스'  in nouns:
        return 26
    elif '경영학' in nouns:
        return 27
    elif 'Endicott자유' in nouns or '자유' in nouns:
        return 28
    elif '자기설계' in nouns or '자기' in nouns or '설계' in nouns:
        return 29
    elif '글로벌철도' in nouns:
        return 30
    elif '철도건설시스템' in nouns or '철도건설' in nouns or '철건' in nouns or '건설'in nouns:
        return 31
    elif '철도경영' in nouns or '철경' in nouns:
        return 32
    elif '물류시스템' in nouns or '물류' in nouns:
        return 33
    elif '철도전기시스템' in nouns or '철도전기' in nouns or '철전' in nouns:
        return 34
    elif '철도소프트웨어' in nouns or '소프트웨어' in nouns:
        return 35
    elif '철도차량시스템' in nouns or'철도차량' in nouns or '철차' in nouns or '차량' in nouns:
        return 36
    elif '건축' in nouns:
        return 37
    elif '우송디젯철도아카메디' in nouns or '디젯철도아카데미' in nouns:
        return 38
    elif 'IT보안' in nouns or 'IT' in nouns or '보안' in nouns:
        return 39
    elif '글로벌미디어영상' in nouns or '글미' in nouns or '미' in nouns or '디어' in nouns or '영상' in nouns:
        return 40
    elif '게임멀티미디어' in nouns or '겜멀' in nouns or '게임' in nouns or '멀티미디어' in nouns:
        return 41
    elif '미디어디자인영상' in nouns or '미디' in nouns or '미디어' in nouns or '디자인' in nouns:
        return 42
    elif '글로벌조리' in nouns or '글조' in nouns:
        return 43
    elif '폴보퀴즈조리' in nouns or '폴보' in nouns or '퀴즈' in nouns:
        return 44
    elif '글로벌외식창업' in nouns or '창업' in nouns:
        return 45
    elif '외식조리' in nouns or '외조' in nouns:
        return 46
    elif '한식조리과학' in nouns or '한조' in nouns or '한식' in nouns:
        return 47
    elif '외식조리경영' in nouns or '외조경' in nouns:
        return 48
    elif '식품영양학' in nouns or '식품' in nouns or '영양학' in nouns:
        return 49
    elif '바이오식품과학' in nouns or '바이오' in nouns:
        return 50
    elif '호텔관광경영' in nouns or '호경' in nouns or '호텔' in nouns or '관광' in nouns:
        return 51
    elif '사회복지학과' in nouns or '사복' in nouns or '사회복지학' in nouns:
        return 52
    elif '작업치료학과' in nouns or '작치' in nouns:
        return 53
    elif '언어치료전공' in nouns or '언어' in nouns:
        return 54
    elif '청강학전공' in nouns or '청강학' in nouns or '청강' in nouns:
        return 55
    elif '보건의료경영' in nouns or '보의경' in nouns or '보건' in nouns or '의료' in nouns:
        return 56
    elif '유아교육' in nouns or '유교' in nouns or '유교과' in nouns:
        return 57
    elif '뷰티디자인경영' in nouns or '뷰티' in nouns or '디자인' in nouns:
        return 58
    elif '응급구조' in nouns or '응구' in nouns or '응급' in nouns or '구조' in nouns:
        return 59
    elif '소방방재' in nouns or '소방' in nouns or '방재' in nouns:
        return 60
    elif '안전공학' in nouns or '안전' in nouns or '공학' in nouns:
        return 61
    elif '간호학' in nouns or '간호' in nouns:
        return 62
    elif '물리치료' in nouns or '물치' in nouns:
        return 63
    elif '스포츠건강재활' in nouns or '스건' in nouns or '건강' in nouns or '재활' in nouns:
        return 64
    elif '세무부동산' in nouns or '세무' in nouns or '부동산' in nouns:
        return 65
    elif 'w1' in nouns:
        return 66
    elif 'w2' in nouns:
        return 67
    elif 'w3' in nouns:
        return 68
    elif 'w4' in nouns:
        return 69
    elif 'w5' in nouns:
        return 70
    elif 'w6' in nouns:
        return 71
    elif 'w7' in nouns:
        return 72
    elif 'w8' in nouns:
        return 73
    elif 'w9' in nouns:
        return 74
    elif 'w10' in nouns:
        return 75
    elif 'w11' in nouns:
        return 76
    elif 'w12' in nouns:
        return 77
    elif 'w13' in nouns:
        return 78
    elif 'w14' in nouns:
        return 79
    elif 'w15' in nouns:
        return 80
    elif 'w16' in nouns:
        return 81 
    elif 'w17' in nouns:
        return 82
    elif 'w18' in nouns:
        return 83
    elif 'w19' in nouns:
        return 84    