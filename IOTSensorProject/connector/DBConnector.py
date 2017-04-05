import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='10.207.3.0', port=3306, user='quaria', password='debiancolasininen', db='sensor_data', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def insert():
	with connection.cursor() as cursor:
        #Create a new record
		sql = "INSERT INTO raw_data (state) VALUES (%s)"
		cursor.execute(sql, ('1'))
       
		#Connection is not autocommit by default so you must commit to save
		#your settings
		connection.commit()
