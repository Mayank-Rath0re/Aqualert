import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="root",database="aqualert")
cursor=db.cursor()
def inp_data():
    pass
def rollback():
    pass
def main():
    while True:
        print("1. Enter Data")
        print("2. Rollback Last Function")
        print("3. Exit")
        ask = int(input("Enter S.No. Of Function: "))
        if ask==1:
            inp_data()
        elif ask==2:
            rollback()
        elif ask==3:
            break
        else:
            print("Invalid Input")
main()