# 김경호 작업공간
# 형태소 분석 결과 리턴 기능

# 리스트 요소 갯수 구하기 위함
from collections import Counter
# 형태소 분석 위함
from konlpy.tag import Komoran
komoran = Komoran()

text = input('학교 관련? 시설 관련? : ')
tree = komoran.nouns(text) # 입력 받은 문장에서 명사만 추출
counter1 = Counter(tree) # 추출한 명사들의 출현 횟수
counter2 = tree.count('학교') # 추출한 명사들 중에 학교라는 단어가 몇번 나왔는지
if '학교' in tree:
    print('형태소 분석 결과 : ', end='')
    print(tree)
    print(counter1)
    print(counter2)
    print('학교 관련 분기로 이동')
elif '시설' in tree:
    print('형태소 분석 결과 : ', end='')
    print(tree)
    print(counter1)
    print('시설 관련 분기로 이동')
else:
    print('형태소 분석 결과 : ', end='')
    print(tree)
    print(counter1)
    print('다시 질문 유도')