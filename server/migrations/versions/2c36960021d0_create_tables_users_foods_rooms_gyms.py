"""Create tables users,foods,rooms,gyms

Revision ID: 2c36960021d0
Revises: 6abebcc7fadd
Create Date: 2023-07-04 11:44:34.785598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c36960021d0'
down_revision = '6abebcc7fadd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', sa.Integer(), nullable=True))
        batch_op.drop_column('phone')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.INTEGER(), nullable=True))
        batch_op.drop_column('telephone')

    # ### end Alembic commands ###