from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# sets the name of your app to the name of your module ("app" if "app.py" is the name of your file).
app = Flask(__name__)
# In this case, @app.route is a Python decorator.
#  Decorators take functions and returns another
# function, usually extending the input function
# with additional ("decorated") functionality.
# @app.route is a decorator that takes an input
# function index()as the callback that gets invoked
# when a request to route / comes in from a client.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:16760@localhost:5432/ardeshir'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# create class through db.model which maps classes to tables via sqlalchemy orm


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # for easier debuging in interactive python or .. add followin

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'


db.create_all()


@app.route('/')
def index():
    # fetch(query) from table person the fist row and then name column
    person = Person.query.first()
    return "helloo" + person.name
# watch mode run in terminal following:
# $ FLASK_APP=app.py FLASK_DEBUG=true flask run
# if __name__ == '__main__':
#   app.run()
