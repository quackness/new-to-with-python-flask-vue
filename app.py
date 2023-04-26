# save this as app.py
from flask import Flask
from flask import render_template

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from config import Config


load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()


@app.route("/")
def index():
    name = 'John Smith'
    return render_template('index.html', name=name)


with app.app_context():
    db.create_all()
