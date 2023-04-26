# save this as app.py
from flask import Flask
from flask import render_template
from dotenv import load_dotenv


load_dotenv('./.flaskenv')

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route("/")
def index():
    name = 'John Smith'
    return render_template('index.html', name=name)
