from flask import Flask, render_template, request
from pymongo import MongoClient
import jsonify
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
@app.route('/')
def survey_form():
    return render_template('survey_form.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    gender = request.form['gender']
    feedback = request.form['feedback']

@app.route('/add_data')
def add_data():
    mycollection = db['mycollection']
    data = {'name': 'John', 'age': 25}
    mycollection.insert_one(data)
    return 'Data added successfully'


@app.route('/get_data')
def get_data():
    mycollection = db['mycollection']
    data = mycollection.find()
    result = []
    for d in data:
        result.append({'name': d['name'], 'age': d['age']})
    return jsonify(result)
    # Save the survey data to a database or send it via email
    # ...

    return 'Thank you for submitting the survey!'

if __name__ == '__main__':
    app.run(debug=True, port=58472)
