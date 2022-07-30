import mysql.connector
import mysql_config as c

cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database='test')
cursor = cnx.cursor()