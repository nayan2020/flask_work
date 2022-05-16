from pypi_org.data.users import User
from pypi_org.data import db_session


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()
