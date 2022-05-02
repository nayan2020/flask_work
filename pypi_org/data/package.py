import datetime
import sqlalchemy as sa
# import sqlalchemy.orm as orm
#
# from data.releases import Release
# from sqlalchemy.ext.declarative import declarative_base
from pypi_org.data.modelbase import SqlAlchemyBase


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    # releases = orm.relation("Release", order_by=[
    #     Release.major_ver.desc(),
    #     Release.minor_ver.desc(),
    #     Release.build_ver.desc(),
    # ], back_populates='package')

    def __repr__(self) -> str:
        return '<package {}>'.format(self.id)
