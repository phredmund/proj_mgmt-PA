import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('new_risk', __name__, url_prefix='/')


@bp.route('/new_risk', methods=('GET', 'POST'))
def new_risk():
    if request.method == 'POST':
        risk_name = request.form['risk_name']
        description = request.form['description']
        severity = request.form['severity']
        proj_name = request.form['proj_name']
        db = get_db()
        error = None

        if not risk_name:
            error = 'Risk name is required'
        elif not description:
            error = 'Risk description is required'
        elif not severity:
            error = 'Severity is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO risks (risk_name, description, severity, project_name, mitigated) VALUES (?, ?, ?, ?, 0)",
                    (risk_name, description, severity, proj_name)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Project {risk_name} already exists."
            else:
                return redirect(url_for("new_risk.new_risk"))

        flash(error)

    return render_template('new_risk.html')
