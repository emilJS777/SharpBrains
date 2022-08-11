"""adf

Revision ID: c7eee11396e4
Revises: 98bf1cc74cb0
Create Date: 2022-08-06 18:22:48.460144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7eee11396e4'
down_revision = '98bf1cc74cb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_status')
    # ### end Alembic commands ###
