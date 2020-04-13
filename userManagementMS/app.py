
from flask import Flask, request, make_response,jsonify
import models.model as model
import datetime
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/USER_MANAGER_DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route("/user")
def hello():
    return {"hello": "user manager"}

@app.route("/user/<string:user>")
def user_exists(user):
    query_user = model.UserManagerDB.query.filter_by(username=user).first()
    if query_user:
        return "User exists - true", 201
    else:
        return "User does not exists - false", 401

@app.route("/user/register", methods=['POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = model.UserManagerDB(
                data['name'],
                data['username'],
                data['password'],
            )
        response = user_exists(data['username'])
        if response[1] == 401:
            new_user.save_to_db()
            return "saved to record - true", 201
        else:
            return "didnt saved to record- already present false", 401

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
    model.manager.run()
