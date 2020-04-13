# def encode_auth_token(self,username):
#     try:
#         payload = {
#             'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=30),
#             'iat' : datetime.datetime.utcnow(),
#             'sub' : username
#         }
#         return jwt.encode(
#             payload,
#             app.config.get('SECRET_KEY'),
#             algorithm = 'HS256'
#         )
#     except Exception as e:
#         return e

from werkzeug.security import safe_str_cmp
import requests

def authenticate(username, password):
    user = requests.get('http://127.0.0.1:5000/user/' + username)
    if user[0] and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)