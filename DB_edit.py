import mysql.connector
import csv
Coordinates={}
max_key=0
db = mysql.connector.connect(host="localhost",user="root",password="root",database="aqualert")
cursor=db.cursor()
def get_max_sno():
    cursor.execute("SELECT MAX(SNo) FROM species;")
    for i in cursor:
        if i[0]==None:
            max_key=0
        else:
            max_key=i[0]
    return max_key

def csv_store():
    file=open("coordinates.csv","r")
    csv_reader=csv.reader(file)
    for i in csv_reader:
        print(i)
        Coordinates[i[0]]=[(i[1],i[3]),(i[2],i[4])]
    file.close()

def inp_data():
    global max_key
    Name=input("Enter Species Name: ")
    duration=input("When are they found: ")
    n=int(input("Enter No. of Regions for the species: "))
    for i in range(n):
        region=input(f"Enter Region {i+1}: ")
        if region not in Coordinates:
            print(region," not found in coordinates")
        else:
            final_query=f"INSERT INTO species VALUES({max_key+1},\"{Name}\",{Coordinates[region][0][0]},{Coordinates[region][1][0]},{Coordinates[region][0][1]},{Coordinates[region][1][1]},\"{region}\",\"{duration}\");"
            cursor.execute(final_query)
            max_key+=1
    db.commit()

    
def rollback():
    ask=input("Are you sure you want to rollback? (Yes/Any other key): ")
    if "Y" in ask.upper():
        db.rollback()
        print("Rollbacked Successfully !")
    else:
        print("Rollback Cancelled")


def main():
    global max_key
    csv_store()
    max_key=int(get_max_sno())
    print(Coordinates.keys())
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