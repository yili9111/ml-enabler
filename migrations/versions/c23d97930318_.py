"""empty message

Revision ID: c23d97930318
Revises: 
Create Date: 2019-05-17 16:31:19.931667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c23d97930318'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ml_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('dockerhub_url', sa.String(), nullable=True),
    sa.Column('dockerhub_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ml_models')
    # ### end Alembic commands ###
