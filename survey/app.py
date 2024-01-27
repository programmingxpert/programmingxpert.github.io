from flask import Flask, request, render_template
from pymongo import MongoClient
import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

app = Flask(__name__)
client = MongoClient("mongodb+srv://Puski:satya%40123@cluster0.quz6u.mongodb.net")
db = client["surveys"]
collection = db["responses"]
app.static_folder = 'static'
@app.route("/")
def index():
    return render_template("survey.html")

@app.route("/submit-form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    myCheckbox = request.form.get("myCheckbox")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    checkbox = request.form.get("Checkbox")

    data = {
        "name": name,
        "email": email,
        "age": age,
        "What do you think of Genshin Impact?": q1,
        "What do you think of Valorant/Fortnite?": q2,
        "Game style": checkbox,
        "Genre": myCheckbox,
        "What's your favortite anime":q3,
        "If you ever had any good storyline":q4
    }

    collection.insert_one(data)

    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run(port=58472, debug=True)

    
