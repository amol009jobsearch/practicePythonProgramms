import pymysql

connection = pymysql.connect(user='root', passwd='root', host='localhost', database='customerinformation')
cursor = connection.cursor()
query = ("select * from customerinfo where customerid=1")
updatequery = ("update customerinfo set customername='Maria' where customerid=1")
cursor.execute(updatequery)
connection.commit()
print(cursor.rownumber, "record(s) affected")
query = ("select * from customerinfo where customerid=1")
cursor.execute(query)
cursor.close()
for item in cursor:
    print(item)