# 22.11.14 김경호

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='qlalfqjsgh1!', db='chatDB', charset='utf8')
cur = conn.cursor()

sql_create_level1 = '''
    CREATE TABLE level1 (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        question VARCHAR(20) NOT NULL,
        PRIMARY KEY(id)
    )
'''
sql_create_level2 = '''
    CREATE TABLE level2 (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        question VARCHAR(20) NOT NULL,
        table1_id INT UNSIGNED NOT NULL,
        PRIMARY KEY(id)
    )
'''

level1_vals = [['학교'], ['시설']]
level2_vals = [['학과', 1], ['학사', 1], ['건물 위치', 2]]
with cur:
    cur.execute('DROP TABLE IF EXISTS level1')
    cur.execute('DROP TABLE IF EXISTS level2')
    cur.execute(sql_create_level1)
    cur.execute(sql_create_level2)
    cur.executemany("INSERT INTO level1(question) VALUES(%s)", level1_vals)
    cur.executemany("INSERT INTO level2(question, table1_id) VALUES(%s, %s)", level2_vals)

conn.commit()
conn.close()