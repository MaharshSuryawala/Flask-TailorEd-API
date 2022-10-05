from flask import Flask
from flaskext.mysql import MySQL
import json
from flask import jsonify

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pw'
app.config['MYSQL_DATABASE_DB'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'host'
mysql.init_app(app)

conn = mysql.connect()
cursor= conn.cursor()

cursor.execute("SHOW TABLES;")
print(cursor.fetchall())

#GET
@app.route('/tailored/activity_t')

def activity():
    cursor.execute("SELECT * from activity_t;")
    data=cursor.fetchall()
    '''
    columns = cursor.description
    data=["hi"]
    result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
    column_list=result[0].keys()
    print(column_list)
    '''
    return json.dumps(data)


@app.route('/tailored/course_t')
def course():
    cursor.execute("SELECT * from course_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/courseactivity_t')
def courseactivity():
    cursor.execute("SELECT * from courseactivity_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/coursegrade_t')
def coursegrade():
    cursor.execute("SELECT * from coursegrade_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/courselayout_t')
def courselayout():
    cursor.execute("SELECT * from courselayout_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/courseterm_t')
def courseterm():
    cursor.execute("SELECT * from courseterm_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/department_t')
def department():
    cursor.execute("SELECT * from department_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/faculty_t')
def faculty():
    cursor.execute("SELECT * from faculty_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/facultyactivity_t')
def facultyactivity():
    cursor.execute("SELECT * from facultyactivity_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/facultydepartment_t')
def facultydepartment():
    cursor.execute("SELECT * from facultydepartment_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/layout_t')
def layout():
    cursor.execute("SELECT * from layout_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/major_t')
def major():
    cursor.execute("SELECT * from major_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/majordepartment_t')
def majordepartment():
    cursor.execute("SELECT * from majordepartment_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/photossorted_t')
def photossorted():
    cursor.execute("SELECT * from photossorted_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/room_t')
def room():
    cursor.execute("SELECT * from room_t;")
    data=cursor.fetchall()
    return json.dumps(data)


@app.route('/tailored/roomlayout_t')
def roomlayout():
    cursor.execute("SELECT * from roomlayout_t;")
    data=cursor.fetchall()
    return json.dumps(data)


@app.route('/tailored/roomtechnologyused_t')
def roomtechnologyused():
    cursor.execute("SELECT * from roomtechnologyused_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/student_graduate_t')
def student_graduate():
    cursor.execute("SELECT * from student_graduate_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/student_t')
def student():
    cursor.execute("SELECT * from student_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/student_undergraduate_t')
def student_undergraduate():
    cursor.execute("SELECT * from student_undergraduate_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/studentcourse_t')
def studentcourse():
    cursor.execute("SELECT * from studentcourse_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/studentethnicity_t')
def studentethnicity():
    cursor.execute("SELECT * from studentethnicity_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/studentmajor_t')
def studentmajor():
    cursor.execute("SELECT * from studentmajor_t;")
    data=cursor.fetchall()
    return json.dumps(data)

@app.route('/tailored/technologyused_t')
def technologyused():
    cursor.execute("SELECT * from technologyused_t;")
    data=cursor.fetchall()
    return json.dumps(data)
