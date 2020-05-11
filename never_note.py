from flask import jsonify, render_template


def render_note_desk():
    return render_template(
        "never_note.html"
    )
