import pymysql

db = pymysql.connect("localhost",port=3306,user="root",
                     passwd="123456",database="stu",charset="utf8")

cur = db.cursor()

