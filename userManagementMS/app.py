
from flask import Flask, request, make_response,jsonify,Blueprint,current_app
import models.model as model
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/USER_MANAGER_DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "123456"

def token_required(allow_permission):
    # @wraps(f)
    def inner_decorator(f):
        def _verify(*args, **kwargs):
            auth_headers = request.headers.get('Authorization', ' ').split()
            print(auth_headers)
            invalid_msg = {
                'message': 'Invalid token. Registeration and / or authentication required',
                'authenticated': False
            }
            expired_msg = {
                'message': 'Expired token. Reauthentication required.',
                'authenticated': False
            }
            if len(auth_headers) != 2:
                return jsonify(invalid_msg), 401

            try:
                token = auth_headers[1]
                data = jwt.decode(token, current_app.config['SECRET_KEY'])
                print(data)
                user = model.UserManagerDB.query.filter_by(username=data['username']).first()
                print("2")
                if data['permission'] != allow_permission:
                    raise RuntimeError('User not authorize to register new user')
                if not user:
                    raise RuntimeError('User not found')
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
            except (jwt.InvalidTokenError, Exception) as e:
                print(e)
                return jsonify(invalid_msg), 401
        return _verify
    return inner_decorator

@app.route("/user/register", methods=['POST'])
@token_required('create')
def register_user():
    data = request.get_json()
    user = model.UserManagerDB(**data)
    print(user)
    user.save_to_db()
    return jsonify(user.json()), 201

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





if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    model.manager.run()
