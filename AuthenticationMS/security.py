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
    if user[2].username and safe_str_cmp(user[2].password, password):
        return user.username

def identity(payload):
    user_id = payload['id']
    userstatus = requests.get('http://127.0.0.1:5000/user/find_user_by_id/' + user_id)
    return userstatus

