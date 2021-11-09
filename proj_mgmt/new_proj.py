import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('new_proj', __name__, url_prefix='/')


@bp.route('/new_proj', methods=('GET', 'POST'))
def new_proj():
    if request.method == 'POST':
        proj_name = request.form['proj_name']
        description = request.form['description']
        manager = request.form['manager']
        db = get_db()
        error = None

        if not proj_name:
            error = 'Project name is required'
        elif not description:
            error = 'Project description is required'
        elif not manager:
            error = 'Project manager is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO project (proj_name, description, manager) VALUES (?, ?, ?)",
                    (proj_name, description, manager)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Project {proj_name} already exists."
            else:
                return redirect(url_for("new_proj.new_proj"))

        flash(error)

    return render_template('new_proj.html')