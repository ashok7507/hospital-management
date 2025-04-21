from flask import Flask, render_template, request, redirect
import database  # importing your separate db file

app = Flask(__name__)

# Ensure DB table exists
database.create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    disease = request.form['disease']
    database.add_patient(name, age, disease)
    return redirect('/view')

@app.route('/view')
def view_patients():
    patients = database.get_all_patients()
    return render_template('view.html', patients=patients)

@app.route('/delete/<int:id>')
def delete(id):
    database.delete_patient(id)
    return redirect('/view')

if __name__ == '__main__':
    app.run(debug=True)

