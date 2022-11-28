# 22.11.21 김경호
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='qlalfqjsgh1!',db='chatdb',charset='utf8') 

def search(arr):
    cur = conn.cursor()

    with cur:
        cur.execute('USE chatdb;')
        cur.execute('SELECT DISTINCT level4.question FROM level1, level2, level3, level4 WHERE level1.id = {0} and level2.id = {1} and level3.id = {2} and level4.table3_id = {2};'.format(arr[0], arr[1], arr[2]))
        result = cur.fetchone() # 22.11.24 김경호

    conn.commit()
    #conn.close() 

    return result # 22.11.24 김경호