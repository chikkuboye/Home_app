import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'home_db')

mycursor = mydb.cursor()

while(True):
    print('''
            Enter the option below
            1 :Insert
            2 :View
            3 :Search
            4 :Exit
    ''')

    choice = int(input("Enter the choice you need"))

    if(choice == 1):
        print("Enter the details")
        temp = int(input("Enter the temperature"))
        hum = int(input("Enter the humidity"))
        moist = input("Enter the moisture")
        sensor = input("Enter the sensor value")
        sql = "INSERT INTO `home_automation`(`temp`, `humidity`, `moisture`, `date`, `sensor_values`) VALUES(%s,%s,%s,now(),%s)"
        data = (temp,hum,moist,sensor)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==2):
        print('View the data')
        sql = "SELECT `temp`, `humidity`, `moisture`, `date`, `sensor_values` FROM `home_automation`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        #print(tabulate(result,headers=['amount'],tablefmt = "psql"))
        print(tabulate(result,headers=['temp','humidity','moisture','date','sensor_values'],tablefmt="psql"))

    elif(choice==3):
        print("Search the data using the date ")
        date = input("enter the date : ")
        sql = "SELECT `temp`, `humidity`, `moisture`, `date`, `sensor_values` FROM `home_automation` WHERE `date`='"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['temp','humidity','moisture','date','sensor_values'],tablefmt="psql"))

    elif(choice==4):
        break