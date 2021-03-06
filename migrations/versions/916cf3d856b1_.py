"""empty message

Revision ID: 916cf3d856b1
Revises: 30c23ab7dac4
Create Date: 2020-03-31 06:40:40.773207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '916cf3d856b1'
down_revision = '30c23ab7dac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('job', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=128), nullable=False))
    op.add_column('users', sa.Column('phone_number', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'name')
    op.drop_column('users', 'job')
    # ### end Alembic commands ###
