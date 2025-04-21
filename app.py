from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('hospital.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    disease = request.form['disease']
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (name, age, disease) VALUES (?, ?, ?)", (name, age, disease))
    conn.commit()
    conn.close()
    return redirect('/view')

@app.route('/view')
def view():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    conn.close()
    return render_template('view.html', patients=data)

@app.route('/delete/<int:id>')
def delete(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/view')

if __name__ == '__main__':
    conn = connect_db()
    conn.execute('CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, disease TEXT)')
    conn.close()
    app.run(debug=True)
