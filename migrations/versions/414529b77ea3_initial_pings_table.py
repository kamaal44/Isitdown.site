"""initial pings table

Revision ID: 414529b77ea3
Revises: 
Create Date: 2019-01-28 23:57:23.325608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414529b77ea3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_ip', sa.String(length=120), nullable=True),
    sa.Column('host', sa.String(length=120), nullable=True),
    sa.Column('time_stamp', sa.DateTime(), nullable=True),
    sa.Column('isdown', sa.Boolean(), nullable=True),
    sa.Column('response_code', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pings')
    # ### end Alembic commands ###
