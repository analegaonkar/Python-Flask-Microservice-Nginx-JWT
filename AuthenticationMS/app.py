from flask import Flask, request
# import authmodels.model as model
import requests
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/AUTH_DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.secret_key = "artiartiarti"
jwt = JWT(app, authenticate, identity)

@app.route("/")
def hello():
    return {"hello": "auth"}

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            response = requests.get('http://127.0.0.1:5000/user/' + data['username'])
            print(response.status_code)
            if response.status_code == 201:
                return "User found", 201
            else:
                return "User Not found" , 401

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    # model.manager.run()
    app.run(port=5001)