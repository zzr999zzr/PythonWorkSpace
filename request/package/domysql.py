# -*- coding:utf-8 -*-
# Author:lixuecheng

import pymysql
from request.package.logger import log, logger
from request.package.baseClass import baseClass
from sshtunnel import SSHTunnelForwarder


class DoMysql(baseClass):
    @log
    def __init__(self, ip, user, password, dbname, port=3306, is_autocommit=True, is_yun=False, yun_user=None, yun_password=None):
        if is_yun:
            self.ip = ip
            self.user = user
            self.passwd = password
            self.dbname = dbname
            self.port = port
            self.yun_user = yun_user
            self.yun_passwd = yun_password

            self.is_yun = True
        else:
            try:
                self.db = pymysql.connect(host=ip, port=int(port), user=user, password=password,
                                          database=dbname, charset='utf8', autocommit=False)
                self.string = ip + ':' + \
                    str(port) + ',user=' + user + ',password=' + \
                    password + ',database=' + dbname
                self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
                self.status = True
                self.is_auto = is_autocommit
                self.res = []
                logger.info('mysql连接成功，-----' + self.string)
            except Exception as e:
                self.db = None
                self.cursor = False
                self.e = e
                self.string = str(e)
                self.status = False
                raise Exception('数据库连接失败：' + str(e))

    def __str__(self):
        try:
            return 'mysql_' + self.string
        except Exception as e:

            # logger.warn('mysql字符串转化失败，' + str(e))
            return 'mysql,无字符串初始化，获取是日志获取中发生,' + str(e)
            # raise Exception('mysql字符串转化失败，' + str(e))

    @log
    def run(self, sql: str) -> int:
        if self.is_yun:
            count=0

            with SSHTunnelForwarder(
                    (self.ip, self.port),  # 服务器公网IP
                    ssh_password=self.yun_passwd,
                    ssh_username=self.yun_user,
                    remote_bind_address=('localhost', 3306)) as server:  # 服务器私网IP

                print(server)
                print("port=server.local_bind_port:", server.local_bind_port)
                mydb = pymysql.connect(
                    host="127.0.0.1",  # 数据库主机地址
                    port=server.local_bind_port,
                    user=self.user,  # 数据库用户名
                    password=self.passwd,  # 数据库密码
                    database=self.dbname
                )
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                self.res =mycursor.fetchall()
                count=mycursor.rowcount
            return count  

        elif self.status and self.cursor:
            try:
                self.sql = sql
                self.cursor.execute(sql)

                self.res = self.cursor.fetchall()
                if self.is_auto:
                    self.commit()

                return self.cursor.rowcount
            except Exception as e:
                self.e = e
                raise Exception(sql+',执行sql失败，' + str(e))
        else:
            raise Exception('数据库链接失败')

    def close(self):
        if not self.is_yun:
            try:
                self.cursor.close()
                self.db.close()
            except:
                pass
            self.status = False

    def commit(self):
        if not self.is_yun:
            logger.info('执行数据库提交')
            self.db.commit()

    def rollback(self):
        if not self.is_yun:
            logger.info('执行数据库回滚,' + str(self.e))
            self.db.rollback()


# try:
# aa = DoMysql('172.16.9.28', 'root', 'a111111', '')

# print(aa.run('SHOW DATABASES'))
#     # raise Exception('')
#     aa.commit()
# except:
#     aa.rollback()
# aa = DoMysql('172.16.9.28', 'root', 'a111111', 'gtobusinessdb')
# a=aa.run('SELECT * from am_resign ')
# print(a)
