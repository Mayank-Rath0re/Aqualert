import mysql.connector
import datetime
import alert_generate
import location 

Seasons = {"All Year":[1,2,3,4,5,6,7,8,9,10,11,12],"Summer":[5,6,7,8],"Winter":[1,2,11,12],"Spring":[3,4],"Autumn":[9,10]}


def main():
    try:
        file = open("credentials.txt")
        usr,passwd = file.read().split('\n')
        print(usr,passwd)
        file.close()
    except FileNotFoundError:
        usr = input("Enter Username for MySQL: ")
        passwd = input("Enter password for MySQL: ")
        file = open("credentials.txt","w")
        file.write(f"{usr}\n{passwd}")
        file.close()

    db = mysql.connector.connect(host='localhost', user=usr, password=passwd, database='aqualert')
    cursor = db.cursor()
    while True:
        month = datetime.date.today().month
        RNo=0
        species=[]
        final_species=[]
        latitude,longitude = location.get_location()
        cursor.execute(f"SELECT RNo FROM coordinates where {latitude} between Latitude1 and Latitude2 and {longitude} between Longitude1 and Longitude2;")
        for i in cursor:
            if i=='':
                pass
            RNo = i[0]
        print(RNo)
        if RNo==0:
            continue
        else:
            cursor.execute(f"SELECT distinct Name,duration from species where RNo={RNo};")
            for i in cursor:
                if i=='':
                    pass
                else:
                    species.append([i[0],i[1]])
            for i in species:
                if month in Seasons[i[1]]:
                    final_species.append(i[0])
            del species, RNo
            print(final_species)
            alert_generate.mail(final_species)
            continue


main()
