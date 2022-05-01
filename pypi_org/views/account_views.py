import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ########################## INDEX ###################

@blueprint.route('/account')
def index():  # put application's code here
    return flask.render_template('account/index.html')


# ########################## REGISTER ###################

@blueprint.route('/account/register', methods=['GET'])
def register_get():  # put application's code here
    return flask.render_template('account/register.html')


@blueprint.route('/account/register', methods=['POST'])
def register_post():  # put application's code here
    return flask.render_template('account/register.html')


# ########################## LOGIN ###################

@blueprint.route('/account/login', methods=['GET'])
def login_get():  # put application's code here
    return flask.render_template('account/login.html')


@blueprint.route('/account/login', methods=['POST'])
def login_post():  # put application's code here
    return flask.render_template('account/login.html')


# ########################## LOGOUT ###################

@blueprint.route('/account/logout')
def logout():  # put application's code here'
    return {}
