# save this as app.py


from flask import Flask
from flask import render_template
from flask import jsonify

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
    import models
    tasks = models.Task.query.all()
    # return render_template('index.html')
    return jsonify(tasks)


with app.app_context():
    db.create_all()
