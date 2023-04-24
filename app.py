# save this as app.py
from flask import Flask
from dotenv import load_dotenv
load_dotenv('./.flaskenv')

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

# @app.route("/")
# def hello():
#     return "Hello, World!"
