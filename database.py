import sqlite3

conn = sqlite3.connect('database.db')
print ("Apertura de datos");

conn.execute('CREATE TABLE libros (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("tabla de datos");
conn.close()