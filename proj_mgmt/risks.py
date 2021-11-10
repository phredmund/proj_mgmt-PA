import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('risks', __name__, url_prefix='/')


@bp.route('/risks?id=<int:id>', methods=['GET'])
def risks(id):
    db = get_db()
    risks = db.execute(
        'SELECT r.id, risk_name, description, severity, mitigated'
        ' FROM risks r'
        ' WHERE r.project_name = ?'
        ' ORDER BY r.id ASC',
        (id, )
    ).fetchall()
    proj_id = id
    projects = db.execute(
        'SELECT p.id, proj_name'
        ' FROM project p'
        ' WHERE p.id = ?',
        (id, )
    ).fetchone()
    return render_template("risks.html", risks=risks, projects=projects, id=proj_id)
