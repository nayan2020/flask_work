import flask
import pypi_org.services.package_service as package_service
from pypi_org.infrastructure import cookie_auth
from pypi_org.infrastructure.views_modifiers import response
from pypi_org.services import user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='/home/index.html')
def index():  # put application's code here
    return {
        'releases': package_service.get_latest_releases(),
        'package_count': package_service.get_package_count(),
        'release_count': package_service.get_release_count(),
        'user_count': user_service.get_user_count(),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


@blueprint.route('/about')
@response(template_file='/home/about.html')
def about():
    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }
