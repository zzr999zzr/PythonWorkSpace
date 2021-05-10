# -*- coding:utf-8 -*-
# Author:lixuecheng
from request.package.edit import add_globals, add_sqlserver, test, expect,setUp,save_report


add_sqlserver('nam1', '172.16.4.161', 'test', 'AAAaaa1234', 'testtcp')
add_globals({'ttt': 'SearchPosition', 'ddd': 'City'})
s1={'sqlName':'nam1','sql':"SELECT * FROM [dbo].[TCP_Person] where id='9A0E12E5-399A-4B16-A74C-00028E3E5A68'",'save':'test3','name':"Mobile"}
ss=setUp(s1,s1)
a = expect('post', 'http://172.16.112.34:9002/api/EsSearch/${ttt}',
           data='{"Keywords":"","Industry":"","${ddd}":"","Salary":"","UpdateTime":"","Offset":0,"Limit":7}').get('Success1').lenSql('nam1', "SELECT * FROM [dbo].[TCP_Person] where id='9A0E12E5-399A-4B16-A74C-00028E3E5A68${test3}'").save('test1')
b = expect('post', 'http://172.16.112.34:9002/api/EsSearch/${ttt}',
           data='{"Keywords":"","Industry":"","${ddd}":"","Salary":"","UpdateTime":"","Offset":0,"Limit":7}').get('Success').lenSql('nam1', "SELECT * FROM [dbo].[TCP_Person] where id='9A0E12E5-399A-4B16-A74C-00028E3E5A68${test1}'").save('test2')
test('222', a, b,setUp=ss)
test('111', a, b,setUp=ss)
save_report('d:/')

# test('',a,b)
