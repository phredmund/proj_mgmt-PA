import os

import flask
from flask import Flask


def create_app(test_config=None, par1=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'proj_mgmt.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def mainpage():
        return flask.render_template('base.html')

    import proj_mgmt.proj_mgmt.db as db
    db.init_app(app)

    import proj_mgmt.proj_mgmt.new_proj as new_proj
    app.register_blueprint(new_proj.bp)

    import proj_mgmt.proj_mgmt.new_risk as new_risk
    app.register_blueprint(new_risk.bp)

    import proj_mgmt.proj_mgmt.projects as projects
    app.register_blueprint(projects.bp)

    import proj_mgmt.proj_mgmt.time as time
    app.register_blueprint(time.bp)

    import proj_mgmt.proj_mgmt.risks as risks
    app.register_blueprint(risks.bp)

    return app
