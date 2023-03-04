import mysql.connector
Coordinates={}
database_name='aqualert'
max_key=0
db = mysql.connector.connect(host="localhost",user="root",password="root",database=f"{database_name}")
cursor=db.cursor()
def get_max_sno():
    cursor.execute("SELECT MAX(SNo) FROM species;")
    for i in cursor:
        if i[0]==None:
            max_key=0
        else:
            max_key=i[0]
    return max_key

def coordinates_store():   #RNo, Region, Latitude1, Latitude2, Longitude1, Longitude2
    cursor.execute("SELECT * FROM coordinates;")
    for i in cursor:
        Coordinates[i[1]]=(i[0],i[2],i[3],i[4],i[5])

def inp_data():    #SNo, Name, Region, Duration, RNo
    global max_key
    Name=input("Enter Species Name: ")
    duration=input("When are they found: ")
    n=int(input("Enter No. of Regions for the species: "))
    for i in range(n):
        region=input(f"Enter Region {i+1}: ")
        if region not in Coordinates:
            print(region," not found in coordinates")
        else:
            final_query=f"INSERT INTO species VALUES({max_key+1},\"{Name}\",\"{region}\",\"{duration}\",{Coordinates[region][0]});"
            print(final_query)
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
    coordinates_store()
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