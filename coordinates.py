import mysql.connector
database_name="aqualert"
def main():
    mydb = mysql.connector.connect(host='localhost',user='root',password='root',database=f'{database_name}')
    mycursor = mydb.cursor()
    max_rno=0
    mycursor.execute("SELECT MAX(RNo) from coordinates;")
    for i in mycursor:
        if i[0]==None:
            pass
        else:
            max_rno=i[0]
    while True:
        print("1. Add Data")
        print("2. Display")
        print("3. Delete")
        print("4. Exit")
        ask = int(input("Enter input: "))
        if ask==1:
            Region=input("Enter Region: ")
            Latitude1 = float(input("Enter Latitude1: "))
            Latitude2 = float(input("Enter Latitude2: "))
            Longitude1 =  float(input("Enter Longitude1: "))
            Longitude2 = float(input("Enter Longitude2: "))
            query = f"INSERT into coordinates VALUES({max_rno+1},\"{Region}\",{Latitude1},{Latitude2},{Longitude1},{Longitude2});"
            mycursor.execute(query)
        elif ask==2:
            mycursor.execute("SELECT * FROM coordinates;")
            for i in mycursor:
                print(i)
        else:
            break
        mydb.commit()
    mycursor.close()
    mydb.close()
main()