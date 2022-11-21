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
#11-21 조영수 level 2,3,4추가
def logic2(userInput):
    nouns = komoran.nouns(userInput)
    #level2.id 
    if '학과' in nouns:
        return 1
    elif '학사' in nouns:
        return 2
    elif '건물 위치' in nouns:
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
    elif '재입학' in nouns:
        return 3
    elif '자퇴/제적' in nouns:
        return 4
    elif '졸업' in nouns:
        return 5
    elif '복합터미널' in nouns:
        return 6
    elif '대전역' in nouns:
        return 7
    elif '우송도서관' in nouns:
        return 8
    elif '우송유치원' in nouns:
        return 9
    elif '사회봉사단' in nouns:
        return 10    