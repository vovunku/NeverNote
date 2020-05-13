from flask import Flask, jsonify, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import logging
import os
import task
import pathlib
import json

import never_note

app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/tmp'
ALLOWED_EXTENSIONS = {'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

task_list = []

done_tasks_list = []


@app.route('/', methods=['GET'])
def render_site():
    return never_note.render_task_desk(task_list, done_tasks_list)


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
    task_info = request.form.get("task_info")
    task_complexity = request.form.get("task_complexity")
    task_list.append(task.Task(task_date, task_name, task_info, task_complexity, "todo"))
    return redirect('/')


@app.route('/move_right/<task_id>', methods=["POST"])
def move_right(task_id=None):
    task_id = int(task_id)
    try:
        task_list[task_id].move_right()
    except ValueError:
        task_list[task_id].finish()
        done_tasks_list.append(task_list[task_id])
        task_list.pop(task_id)
    return redirect('/')


@app.route('/add_task_sheet', methods=["POST"])
def add_task_sheet():
    file = request.files["task_sheet_name"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    global task_list
    global done_tasks_list
    with open('tmp/' + filename) as inp_file:
        imported = json.load(inp_file)
        task_list, done_tasks_list = never_note.import_sheet(imported)
    return redirect('/')


@app.route('/get_task_sheet', methods=["GET"])
def get_task_sheet():
    return never_note.export_sheet(task_list, done_tasks_list)


if __name__ == '__main__':
    app.run()
