import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('projects', __name__, url_prefix='/')


@bp.route('/projects', methods=['GET'])
def projects():
    db = get_db()
    projects = db.execute(
        'SELECT p.id, proj_name, description, manager'
        ' FROM project p'
        ' ORDER BY p.id ASC'
    ).fetchall()
    return render_template("projects.html", projects=projects)