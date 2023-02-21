import geocoder
import mysql.connector
def get_user_location():
    #Needs to be checked.
    g = geocoder.ip('me')
    return g.latlng

def check_species(location):
    ls_species=[]
    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='aqualert')
    my_cursor=mydb.cursor()
    query = f"SELECT * FROM species where ({location[0]} between Latitude1 and Latitude2) and ({location[1]} between Longitude1 and Longitude2);"
    my_cursor.execute(query)
    for i in my_cursor:
        if i=="":
            continue
        ls_species.append(i)
    if ls_species==[]:
        return False
    return True, ls_species

def alert_user():
    pass

def main():
    location=get_user_location()
    location1=[44.329,-68.1823]
    print(location)
    if check_species(location1)==False:
        pass
    else:
        alert_user()
main()