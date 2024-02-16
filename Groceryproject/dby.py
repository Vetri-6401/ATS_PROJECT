import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',db='sla')
my_cursor=connection.cursor()
my_cursor.execute('select * from records')

data=my_cursor.fetchall()

for i in data:
    print(i)
    print('---------------------------------------------')

connection.close()