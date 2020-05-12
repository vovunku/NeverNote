from flask import Flask, jsonify, request, redirect, send_from_directory
import logging
import os
import task

import never_note

app = Flask(__name__)

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
    print(task_date, task_name, task_info, task_complexity)
    task_list.append(task.Task(task_date, task_name, task_info, task_complexity, "todo"))
    return redirect('/')


@app.route('/move_right/<task_id>', methods=["POST"])
def move_right(task_id=None):
    task_id = int(task_id)
    try:
        task_list[task_id].move_right()
    except ValueError:
        done_tasks_list.append(task_list[task_id])
        task_list.pop(task_id)
    return redirect('/')


if __name__ == '__main__':
    app.run()
