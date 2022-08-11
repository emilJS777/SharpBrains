"""adsf

Revision ID: 5547ef633065
Revises: b02516c66e72
Create Date: 2022-08-07 18:11:31.057059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5547ef633065'
down_revision = 'b02516c66e72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=120), nullable=False),
    sa.Column('main', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_image')
    # ### end Alembic commands ###
