"""create table country

Revision ID: 0f931b54fbbf
Revises: 
Create Date: 2019-10-24 12:44:36.554814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f931b54fbbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'country',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String(64),nullable=False)
    )


def downgrade():
    op.drop_table('country')
