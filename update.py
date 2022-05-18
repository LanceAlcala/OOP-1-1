import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Lance Wesley Alcala\OneDrive\Documents\Database1.accdb;')
    print("Database is connected")

    user_id = 3
    Address = "Cavite"
    database = connection.cursor()
    database.execute('UPDATE Table1 SET Address=? WHERE id=?',(Address,user_id))
    connection.commit()

    user_id = 10
    Fullname = "Lance Wesley B. Alcala"
    Age = "19"
    Course = "BSCPE"
    Address = "Cavite"
    Grade = 100
    database1 = connection.cursor()
    database1.execute('UPDATE Table1 SET Fullname=?,Age=?,Course=?,Address=?,Grade=? WHERE id=?', (Fullname, Age, Course, Address, Grade, user_id))

    connection.commit()
    print("Database is updated")


except pyodbc.Error:
    print("Database is NOT connected")