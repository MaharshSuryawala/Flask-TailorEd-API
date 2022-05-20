from flask import Flask
import mysql.connector

myDb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my-secret-pw",
  database="sql_hr",
  auth_plugin='mysql_native_password'
)

cursor = myDb.cursor()

cursor.execute("SELECT * FROM employees")

result = cursor.fetchall()
print(result)

app = Flask(__name__)


@app.route('/tailored/tablename/column')
def hello_world():
    return "Hello"


if __name__ == '__main__':
    app.run()
