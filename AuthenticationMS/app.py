from flask import Flask, request,jsonify
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


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = requests.post('http://127.0.0.1:5000/user/auth', json = data)
    username = user.json()['username']
    print( user.json()['username'])
    print( username)
    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': username,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        app.config['SECRET_KEY'])
    print("token")
    print(token)
    return jsonify({'token': token.decode('UTF-8')})


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    # model.manager.run()
    app.run(port=5001)