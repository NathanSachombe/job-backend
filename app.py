from flask import Flask, request
from flask_restful import Api
from models import db
from flask_migrate import Migrate
from Resources.users import User

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BUNDLE_ERRORS'] = True

migrations = Migrate( app, db)
db.init_app(app)

api.add_resource(User, '/users', '/users/<int:id>')

@app.route("/")
def index():
    return "<h1>Welcome to Jobs!</h1>"


if __name__=="__main__":
    app.run(port=5555, debug=True)

