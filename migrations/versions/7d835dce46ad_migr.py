"""migr

Revision ID: 7d835dce46ad
Revises: 5c2a327adc55
Create Date: 2022-08-05 11:06:18.141761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d835dce46ad'
down_revision = '5c2a327adc55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('image_path', sa.String(length=120), nullable=True),
    sa.Column('sphere_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sphere_id'], ['sphere.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###