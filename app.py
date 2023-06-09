
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from forms import TaskForm

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
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    # //jsonify() xsend back as a string, this is what the client expects
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_task():
    user_input = request.get_json()
    import models
    form = TaskForm(data=user_input)
    if form.validate():
        task = models.Task(title=form.title.data)
        db.session.add(task)
        db.session.commit()
        return jsonify(task)
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete_task():
    import models
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': 'ok'}), 200


@app.route('/complete', methods=['POST'])
def complete_task():
    import models
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=task_id).first()
    task.complete = True
    db.session.add(task)
    db.session.commit()
    return jsonify({'result': 'ok'}), 200


with app.app_context():
    db.create_all()
