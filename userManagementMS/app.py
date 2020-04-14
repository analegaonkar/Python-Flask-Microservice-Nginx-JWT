
from flask import Flask, request, make_response,jsonify,Blueprint
import models.model as model
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/USER_MANAGER_DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route("/user")
def hello():
    return {"hello": "user manager"}

@app.route("/user/auth",  methods=['POST'])
def call_authenticate():
    data = request.get_json()
    user = model.UserManagerDB.authenticate(data)
    if user:
        return jsonify(user.json()),200
    else:
        return None,404


@app.route("/user/<string:user>")
def user_exists(user):
    query_user = model.UserManagerDB.query.filter_by(username=user).first()
    if query_user:
        return "User exists - true", 201, query_user
    else:
        return "User does not exists - false", 401, None

@app.route("/user/find_user_by_id/<int:user_id>")
def find_user_by_id(user_id):
    query_user = model.UserManagerDB.query.find_by_id(id=user_id)
    if query_user:
        return "true"
    else:
        return "false"

@app.route("/user/register", methods=['POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            user = UserManagerDB(**data)
            # new_user = model.UserManagerDB( data['name'],data['username'],data['password'], )
            user.save_to_db()
            return jsonify(user.to_dict()), 201

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    model.manager.run()
