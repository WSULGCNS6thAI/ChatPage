# 김경호 작업공간
# mysql DB 연결 예제 코드

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='test', charset='utf8')
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