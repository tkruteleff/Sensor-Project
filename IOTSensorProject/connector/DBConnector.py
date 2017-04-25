import pymysql
import pymysql.cursors

visitorCount = 0

# Connect to the database
connection = pymysql.connect(host='10.207.3.0',
                             port=3306,
                             user='quaria',
                             password='debiancolasininen',
                             db='sensor_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def selectAll():
    with connection.cursor() as select:
        # Get all rows
        sqlS = "Select id, state, time FROM raw_data"
        select.execute(sqlS)
    connection.commit()

def insert1():
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO raw_data (state) VALUES (%s)"
        cursor.execute(sql, ('1'))
    connection.commit()


def insert2():
    with connection.cursor() as cursor2:
        # Add 2 to database
        sql2 = "INSERT INTO raw_data (state) VALUES (%s)"
        cursor2.execute(sql2, ('2'))
    connection.commit()
