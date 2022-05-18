import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Lance Wesley Alcala\OneDrive\Documents\Database1.accdb;')

    user_id = 10

    database = connection.cursor()
    database.execute('DELETE from Table1 where id=?',(user_id))
    connection.commit()
    print("Record is deleted")

except pyodbc.Error:
    print("Database is NOT connected")