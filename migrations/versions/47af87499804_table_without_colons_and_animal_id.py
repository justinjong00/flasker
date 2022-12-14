"""table without colons and animal_id

Revision ID: 47af87499804
Revises: bb017f4a5017
Create Date: 2022-12-01 01:04:29.808709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47af87499804'
down_revision = 'bb017f4a5017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adoption', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id'])

    with op.batch_alter_table('allergy', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'allergy'])

    with op.batch_alter_table('application', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['candidate_id', 'date'])

    with op.batch_alter_table('backgroundcheck', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['application_id'])

    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'diagnosis'])

    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'contact', ['info_id'], ['id'])

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'contact', ['info_id'], ['id'])

    with op.batch_alter_table('foster', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'foster_date'])

    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['diagnosis_id', 'operation_type', 'date'])

    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['treatment', 'diagnosis_id'])

    with op.batch_alter_table('vaccination', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'vaccine_type', 'date'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vaccination', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('foster', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('backgroundcheck', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('application', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('allergy', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('adoption', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
