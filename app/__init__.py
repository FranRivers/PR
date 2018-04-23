from flask import redirect, Flask, render_template, session, flash, url_for, g
from flask_sqlalchemy import *
from sqlalchemy import Column, Integer, ForeignKey, String, update
import sqlite3 as sql
app = Flask(__name__)

con = sql.connect('C:/Users/Fran/Desktop/dic.db',check_same_thread=False)

cursor = con.cursor()
print("hola")


@app.route('/')
def inicio():

    return render_template('home.html')

@app.route('/basica', methods=['GET','POST'])
def basica():

    if request.method == 'POST':

        if request.form:
            con = sql.connect('C:/Users/Fran/Desktop/dic.db',check_same_thread=False)
            con.row_factory = sql.Row
            palabra = request.form['palabra']
            cursor.execute("SELECT * FROM words WHERE lacra = ?", ('%' + palabra + '%',))
            return render_template('basica.html')

    return render_template('basica.html')

@app.route('/abierta', methods=['GET','POST'])
def abierta():

    return render_template('abierta.html')
#
# prueba = ('aa')
# cursor.execute("SELECT * FROM words WHERE guna LIKE ?",('%'+prueba+'%',))

# row = cursor.fetchall()
# for x in cursor:
#
#     print("Español ", x[2])
#     print("\n")

print("operacion existosa")

# con.close()

if __name__ == '__main__':
   app.run(debug = True)

