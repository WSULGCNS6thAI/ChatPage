from konlpy.tag import Komoran
komoran = Komoran()

komoran = Komoran()
text = '건물 번호 알려줘'
print(komoran.morphs(text))
print(komoran.pos(text))
print(komoran.nouns(text))
