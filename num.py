import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Emmanuel",
  password="ope12yemi44",
  database="Sapa_bank"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Names(name VARCHAR(255), age VARCHAR(255))")

