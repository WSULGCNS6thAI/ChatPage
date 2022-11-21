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