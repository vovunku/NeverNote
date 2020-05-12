from flask import jsonify, render_template
import json
import task


def render_task_desk(task_list, done_tasks_list):
    print(task_list)
    return render_template(
        "never_note.html",
        task_list=list(enumerate(task_list)),
        done_tasks=list(enumerate(done_tasks_list)),
        done_tasks_count=len(done_tasks_list)
    )


def export_sheet(task_list, done_tasks_list):
    sheet_json = {
        'task_list': [],
        'done_tasks_list': []
    }
    for task in task_list:
        task_json = _jsonify_task(task)
        sheet_json['task_list'].append(task_json)
    for task in done_tasks_list:
        task_json = _jsonify_task(task)
        sheet_json['done_tasks_list'].append(task_json)
    return jsonify(sheet_json)


def _jsonify_task(task):
    task_json = {
        'date': task.date,
        'name': task.name,
        'info': task.info,
        'complexity': task.complexity,
        'state': task.state
    }
    return task_json


def _taskify_json(task_json):
    return task.Task(task_json['date'],
                     task_json['name'],
                     task_json['info'],
                     task_json['complexity'],
                     task_json['state'])


def import_sheet(import_json):
    task_list = []
    done_tasks_list = []
    for task_json in import_json['task_list']:
        task_list.append(_taskify_json(task_json))
    for task_json in import_json['done_tasks_list']:
        done_tasks_list.append(_taskify_json(task_json))
    return [task_list, done_tasks_list]
