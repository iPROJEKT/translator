"""First migration

Revision ID: 374f0414208c
Revises: 
Create Date: 2023-10-06 21:42:32.618478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '374f0414208c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userhistory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('primary_text', sa.String(), nullable=False),
    sa.Column('translate_text', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userhistory')
    # ### end Alembic commands ###
