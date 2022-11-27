from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)



@app.errorhandler(404)
 # @app.errorhandler(405)
def page(e):
  return render_template('estudiante1.html')

# @app.route('/')
#def home():
 # return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('estudiante1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['addr']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO libros (name,addr,city,pin)  VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "enviado"
      except:
           con.rollback()
           msg = " la operación no se pudo realizar "
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/lista')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from estudiantes")
   
   rows = cur.fetchall();
   return render_template("estudiante.html",rows = rows)


if __name__ == '__main__':
   app.run(debug = True)