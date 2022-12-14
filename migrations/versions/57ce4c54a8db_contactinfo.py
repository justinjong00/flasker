"""contactinfo

Revision ID: 57ce4c54a8db
Revises: a749771f9215
Create Date: 2022-11-30 06:35:58.327656

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57ce4c54a8db'
down_revision = 'a749771f9215'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    with op.batch_alter_table('contact_information', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('phone')

    op.drop_table('contact_information')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_information',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('contact_information', schema=None) as batch_op:
        batch_op.create_index('phone', ['phone'], unique=False)
        batch_op.create_index('email', ['email'], unique=False)

    op.drop_table('contact_info')
    # ### end Alembic commands ###
