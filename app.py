from flask import Flask, jsonify, request, redirect, send_from_directory
import logging
import os

import never_note

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return never_note.render_note_desk()


@app.route('/favicon.ico')
def favicon():
    """Handles browser's request for favicon"""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico'
    )


@app.route('/add_task', methods=["POST"])
def add_task():
    task_date = request.form.get("task_date")
    task_name = request.form.get("task_name")
    task = request.form.get("task")
    print(task_date, task_name, task)
    return redirect('/')


if __name__ == '__main__':
    app.run()
