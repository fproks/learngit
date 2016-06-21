import pymysql
conn = pymysql.connect(host='localhost', port=3306,user='linhos',passwd='3537',db='mysql',charset='UTF8')
cur = conn.cursor()
cur.execute("select version()")
for i in cur:
    print(i)
cur.close()
conn.close()