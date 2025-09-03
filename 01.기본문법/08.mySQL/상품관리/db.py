import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='enrudg20@',
    db='shop',
    charset='utf8',  # 'utf-8' 대신 'utf8'을 사용하는 것이 일반적입니다
    cursorclass=pymysql.cursors.DictCursor,
    port=3306
)

cur = con.cursor()