import pymysql
import pymysql.cursors
import Variables
import time

# Connect to the database
connection = pymysql.connect(host='10.207.3.0',
                             port=3306,
                             user='quaria',
                             password='debiancolasininen',
                             db='sensor_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# Gets the last value of the state row and inserts it into the visitorCount variable
def getLastValue():
    with connection.cursor() as select:
        # Get all rows
        sqlS = "SELECT id, state, time FROM raw_data"
        select.execute(sqlS)
        for row in select:
            Variables.visitorCount = "%s" % (row["state"])
    connection.commit()


def insertIncrease():
    with connection.cursor() as cursor:
        # Plus to visitorcount in database
        sql = "INSERT INTO raw_data (state) VALUES (%s)"
        cursor.execute(sql, Variables.visitorCount)
    connection.commit()


def insertDelete():
    with connection.cursor() as cursor2:
        # Minus from visitorcount in database
        sql2 = "INSERT INTO raw_data (state) VALUES (%s)"
        cursor2.execute(sql2, Variables.visitorCount)
    connection.commit()
