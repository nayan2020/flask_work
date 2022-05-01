import os.path
import flask
import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi_org.sqlite'
    )
    db_session.global_init(db_file)


def register_blueprints():
    from views import cms_views
    from views import home_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
