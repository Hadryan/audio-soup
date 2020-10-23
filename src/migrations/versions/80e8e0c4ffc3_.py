"""empty message

Revision ID: 80e8e0c4ffc3
Revises: 
Create Date: 2020-10-20 21:52:36.766112

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '80e8e0c4ffc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('audiofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sample_rate', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.Column('label_id', sa.Integer(), nullable=True),
    sa.Column('text', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.id'], ),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.PrimaryKeyConstraint('id', 'sample_rate')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('audiofile')
    op.drop_table('label')
    op.drop_table('dataset')
    # ### end Alembic commands ###