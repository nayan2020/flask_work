import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from pypi_org.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):  # put application's code'
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():  # put application's code here'
        raise Exception("You Must specify a db file")

    conn_str = 'sqlite:///' + db_file.strip()
    print(f'Connecting to DB with {conn_str}')

    engine = sa.create_engine(conn_str, echo=True)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import pypi_org.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
