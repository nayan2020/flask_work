"""Added last updated

Revision ID: c070d5557d7b
Revises: 
Create Date: 2022-05-16 18:19:32.989469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c070d5557d7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('last_date', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_packages_last_date'), 'packages', ['last_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_packages_last_date'), table_name='packages')
    op.drop_column('packages', 'last_date')
    # ### end Alembic commands ###
