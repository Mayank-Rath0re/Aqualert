import csv
datalist=[]
def store():
    file = open("coordinates.csv")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row == []:
            pass
        else:
            datalist.append(row)
    file.close()
def restore():
    file = open("coordinates.csv", 'w',newline="")
    csv_writer = csv.writer(file)
    csv_writer.writerows(datalist)
    file.close()
def main():
    store()
    try:
        while True:
            print("1. Add Data")
            print("2. Exit")
            ask = int(input("Enter Choice: "))
            if ask==1:
                name=input("Enter Name: ")
                Latitude1=float(input("Latitude 1: "))
                Latitude2=float(input("Latitude 2: "))
                Longitude1=float(input("Longitude 1: "))
                Longitude2=float(input("Longitude 2: "))
                datalist.append([name,Latitude1,Latitude2,Longitude1,Longitude2])
            else:
                break
            restore()
    except:
        restore()
main()