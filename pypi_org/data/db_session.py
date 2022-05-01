import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = True


def global_init(db_file: str):  # put application's code'
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():  # put application's code here'
        raise Exception("You Must specify a db file")

    conn_str = 'sqlite:///' + db_file.strip()

    engine = sa.create_engine(conn_str, echo=False)
    factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from pypi_org.data.package import Package

    SqlAlchemyBase.metadata.create_all(engine)
