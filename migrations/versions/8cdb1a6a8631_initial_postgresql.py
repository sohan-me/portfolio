"""Initial postgresql

Revision ID: 8cdb1a6a8631
Revises: 
Create Date: 2024-08-25 18:17:57.354395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cdb1a6a8631'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Advantage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(length=100), nullable=False),
    sa.Column('proficiency', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('educationalexperience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(length=100), nullable=False),
    sa.Column('institution', sa.String(length=100), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('featuredproject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.Column('project_link', sa.String(length=200), nullable=True),
    sa.Column('tags', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pricing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan_name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('features', sa.Text(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('project_count', sa.String(), nullable=True),
    sa.Column('experience', sa.String(), nullable=True),
    sa.Column('github', sa.String(length=255), nullable=True),
    sa.Column('linkedin', sa.String(length=255), nullable=True),
    sa.Column('twitter', sa.String(length=255), nullable=True),
    sa.Column('instagram', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specialization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(length=100), nullable=False),
    sa.Column('proficiency', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('specialization')
    op.drop_table('profile')
    op.drop_table('pricing')
    op.drop_table('featuredproject')
    op.drop_table('educationalexperience')
    op.drop_table('Advantage')
    # ### end Alembic commands ###
