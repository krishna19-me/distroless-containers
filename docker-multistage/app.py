# app.py
from flask import Flask, jsonify
from faker import Faker
 
app = Flask(__name__)
fake = Faker()
 
@app.route('/random-user', methods=['GET'])
def random_user():
    username = fake.user_name()
    email = fake.email()
    contact = fake.phone_number()
    location = fake.country()
 
    user = {
        'username': username,
        'email': email,
        'contact': contact,
        'location': location
    }
    return jsonify(user)
 
if __name__ == '__main__':
    app.run(debug=True)

