# 22.10.31 김경호 (###)
# 여기부터 (###)
from konlpy.tag import Komoran
komoran = Komoran(userdic='dataset/dic.user') # 22.11.21 김경호 사용자사전 추가
text = 'w1 위치 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))
# 여기까지 (###)

# 22.11.07 김종무 (***)
# 여기부터 (***)
text = '교육 과정 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대까지 어떻게 올수 있어?'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '졸업 기준 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '입학처 전화번호 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '휴학 신청 기간이 언제야?'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대에 어떤 종류의 학과가 있어?'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '편입하고 싶은데 어떻게 해?'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대 지도 좀 볼 수 있어?'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대 체육관 위치 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대 도서관 위치 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대 학군단에 대해 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))

text = '우송대 남녀 비율 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))
# 여기까지 (***)