import flask

# import services.package_service as package_service
from pypi_org.infrastructure.views_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='/home/index.html')
def index():  # put application's code here
    # test_packages = package_service.new_packages()
    return {}


@blueprint.route('/about')
@response(template_file='/home/about.html')
def about():
    return {}
