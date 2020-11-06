from config import config
from datetime import datetime
import pyodbc 

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+config.password+';Trusted_Connection=no;')
cursor = cnxn.cursor()

cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

try:
    print(f'Attempting To Close Cursor At: {current_time}')
    cursor.close()
    print(f'Cursor Closed At: {current_time}')

except Exception as e:
    print(f'We have an error {e}')