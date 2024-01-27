from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

app = Flask(__name__)
client = MongoClient("mongodb+srv://Puski:satya%40123@cluster0.quz6u.mongodb.net")
db = client["users"]
collection = db["users"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_data():
    data = {
        'emailId': request.form['userEmail'],
        'phoneNumber': request.form['userContact'],
        'password': request.form['userPassword'],
        'gender': 'Male' if request.form.get('genderMale') else 'Female',
    }
    result = collection.insert_one(data)
    response_data = {'id': str(result.inserted_id)}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=58472, debug=True)
