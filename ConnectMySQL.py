#!-*- /usr/bin/python -*-
#!-*- coding = utf-8 -*-
#@Athor : Alfa
#@TIME : 2020/4/10 0010 16:30
#@FILE : ConnectMySQL.PY

import pymysql
"""
实现mysql数据库链接
实现增删改查功能方法
"""



# def conmysql(hostname, username, password, dbname, port, charset='utf8'):
def conmysql(hostname, username, password, dbname, port):

    db = pymysql.connect(hostname, username, password, dbname, port)

    cursor = db.cursor()

    return cursor

def selectData(sql, cursor):
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return results

if __name__ == '__main__':
    hostname = '47.98.185.206'
    dbcursor = conmysql(hostname, username='root', password='Asdf1@34', dbname='Cloudmeeting', port=22)
    sql = "select * from smsdetail where phone='13700840000';"
    results = dbcursor.selectData(sql, dbcursor)
    print(results)











