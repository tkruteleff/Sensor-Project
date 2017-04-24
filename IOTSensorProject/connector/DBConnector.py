import pymysql
import pymysql.cursors


# Connect to the database
connection = pymysql.connect (host = '10.207.3.0',
                                port = 3306,
                                user ='quaria',
                                password = 'debiancolasininen',
                                db = 'sensor_data',
                                charset = 'utf8mb4',
                                cursorclass = pymysql.cursors.DictCursor)

try:
        with connection.cursor() as cursor:
        #Create a new record
            sql = "INSERT INTO raw_data (state) VALUES (%s)"
            cursor.execute(sql, ('1'))
        connection.commit()
        #Read a single record
        with connection.cursor() as cursor:
            sql = "SELECT id, state FROM raw_data WHERE state = %s"
            cursor.execute(sql, ("1",))
            result = cursor.fetchone()
            print(result)

finally:
        connection.close()
