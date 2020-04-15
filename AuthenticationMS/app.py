from flask import Flask, request,jsonify,current_app
# import authmodels.model as model
import requests
import jwt
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/AUTH_DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "123456"
@app.route("/")
def hello():
    return {"hello": "auth"}
'''
this is a sample role dict.Generally the role , permissions
 and username are stored in authorization table or
we can create a new microservice called authorization
'''
role_dict1 ={'admin' : 'create', 'employee' : 'view'}

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = requests.post('http://127.0.0.1:5000/user/auth', json = data)
    username = user.json()['username']
    print( user.json()['username'])
    print( username)
    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    if username == 'Artin':
        role = 'admin'
        permission = role_dict1[role]
    else:
        role = 'employee'
        permission = role_dict1[role]

    token = jwt.encode({
        'iss': "Authentication microservice",
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30),
        'username': username,
        'role': role,
        'permission' : permission},
        current_app.config['SECRET_KEY'])
    print("token")
    print(token)
    return jsonify({'token': token.decode('UTF-8')})


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    # model.manager.run()
    app.run(port=5001)