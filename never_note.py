from flask import jsonify, render_template


def render_task_desk(task_list):
    print(task_list)
    return render_template(
        "never_note.html",
        task_list=list(enumerate(task_list))
    )
