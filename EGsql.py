from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'transports'
)


if con:
    print("connected")
else:
    print("not connected")


def insert (NAME,AGE,CITY):
    res = con.cursor()
    sql = "insert into users (NAME,AGE,CITY) values (%s,%s,%s)"
    user= (NAME,AGE,CITY)
    res.execute(sql,user)
    con.commit()
    print("Data insert Success")

def update (NAME,AGE,CITY,ID):
    res = con.cursor()
    sql = "update users set NAME=%s, AGE = %s, CITY = %s where ID = %s"
    user = (NAME,AGE,CITY,ID)
    res.execute(sql, user)
    con.commit()
    print("Data update Success")

def select ():
    res = con.cursor()
    sql = "Select NAME,AGE,CITY,ID from users"
    res.execute(sql)
    #result = res.fetchone()
    #result = res. fetchmany(2)
    result = res.fetchall()
    #print(result)
    print(tabulate(result,headers=["NAME","AGE","CITY","ID"]))

def delete (ID):
    res = con.cursor()
    sql = "delete from users where ID=%s"
    user = (ID,)
    res.execute(sql, user)
    con.commit()
    print("Data delete Success")

while True:
    print("1. Insert data")
    print("2. Update data")
    print("3. Select data")
    print("4. Delete data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        NAME = input("Enter Name: ")
        AGE= input("Enter Age: ")
        CITY = input("Enter city: ")
        insert(NAME,AGE,CITY)
    elif choice == 2:
        ID = input("Enter Id:")
        NAME = input("Enter Name: ")
        AGE = input("Enter Age: ")
        CITY = input("Enter city: ")
        update(NAME,AGE,CITY,ID)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter the id to delete: ")
        delete(ID)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection. Please try again")

