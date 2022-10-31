# 김경호 작업공간

#from konlpy.tag import Komoran
#komoran = Komoran()

#text = input('질문을 입력하세요 : ')
#print(komoran.nouns(text))

########################################

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='chatDB', charset='utf8')
cur = conn.cursor()
sql_level1 = '''
    CREATE TABLE level1 (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    question VARCHAR(20) NOT NULL,
    PRIMARY KEY(id)
    );
'''
sql_level2 = '''
    CREATE TABLE level2 (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        question VARCHAR(20) NOT NULL,
        table1_id INT UNSIGNED NOT NULL,
        PRIMARY KEY(id)
    );
'''

cur.execute(sql_level1)
conn.commit()
    
conn.close()