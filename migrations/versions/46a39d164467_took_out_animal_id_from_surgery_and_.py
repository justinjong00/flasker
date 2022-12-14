"""took out animal id from surgery and treatment

Revision ID: 46a39d164467
Revises: 360beae11354
Create Date: 2022-11-30 23:34:35.840061

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46a39d164467'
down_revision = '360beae11354'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.drop_column('animal_id')

    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.drop_column('animal_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('animal_id', mysql.INTEGER(), autoincrement=False, nullable=False))

    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.add_column(sa.Column('animal_id', mysql.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
