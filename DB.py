import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="199603",
    database="test_1"

)

mycursor=mydb.cursor()
# sql="CREATE TABLE user(name VARCHAR (20),password VARCHAR (20))"
# sql="INSERT INTO user (name,password) VALUES (%$,%$)"
# user1=("brana","brana1")
# mycursor.execute(sql,user1)
# mydb.commit()
sql="SHOW TABLES"
mycursor.execute(sql)
for db in mycursor:
    print(db)