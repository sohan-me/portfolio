"""Initial migration after reset

Revision ID: 02067d514151
Revises: edaafbcc43a2
Create Date: 2024-08-24 15:01:45.655822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02067d514151'
down_revision = 'edaafbcc43a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_count', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('experience', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.drop_column('experience')
        batch_op.drop_column('project_count')

    # ### end Alembic commands ###
