"""create table crypto_currency

Revision ID: 21a398f4b70c
Revises: abe5d532f2a8
Create Date: 2019-10-24 15:32:08.266374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a398f4b70c'
down_revision = 'abe5d532f2a8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cryptocurrency',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String(255),nullable=False),
        sa.Column('code',sa.String(16),unique=True,nullable=False),
        sa.Column('options',sa.JSON,nullable=False),
        sa.Column('is_active',sa.Boolean,default=True)
    )


def downgrade():
    op.drop_table('cryptocurrency')
