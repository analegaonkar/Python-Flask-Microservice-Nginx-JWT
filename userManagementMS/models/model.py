# import ..app.db as db
from app import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class UserManagerDB(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def json(self):
        return {'name': self.name, 'username': self.username}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
