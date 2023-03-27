import mysql.connector
import csv

usr = input("Enter Username of local MySQL: ")
passwd = input("Enter Password of local MySQL: ")
db = mysql.connector.connect(host="localhost",user=usr,password=passwd)
cursor = db.cursor()

cursor.execute("create database aqualert;")
cursor.execute("use aqualert;")
cursor.execute("create table species(SNo integer primary key, Name varchar(40), Region varchar(25),duration varchar(10), RNo integer);")

file = open("species.csv","r")
csv_reader = csv.reader(file)
for i in csv_reader:
    cursor.execute(f"insert into species values({i[0]},{i[1]},{i[2]},{i[3]},{i[4]});")
file.close()

cursor.execute("create table coordinates(RNo integer primary key, Region varchar(25), Latitude1 decimal(10,6), Latitude2 decimal(10,6), Longitude decimal(10,6), Longitude decimal(10,6));")
file = open("coordinates.csv","r")
csv_reader = csv.reader(file)
for i in csv_reader:
    cursor.execute(f"insert into species values({i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]});")
file.close()

db.commit()
cursor.close()
db.close()