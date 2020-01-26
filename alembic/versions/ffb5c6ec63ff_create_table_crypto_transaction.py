"""create table crypto_transaction

Revision ID: ffb5c6ec63ff
Revises: 522636169598
Create Date: 2019-11-02 16:50:05.152019

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'ffb5c6ec63ff'
down_revision = '522636169598'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'crypto_transaction',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('hash',sa.String(256),unique=True),
        sa.Column('block_number',sa.BigInteger,nullable=False),
        sa.Column('amount',sa.Float,nullable=False),
        sa.Column('time',sa.Time,nullable=False),
        sa.Column('fee',sa.Float,nullable=False),
        sa.Column('meta',sa.JSON),
        sa.Column('confirmations',sa.SmallInteger,default=0,nullable=False),
        sa.Column('status',sa.SmallInteger),
        sa.Column('created_at',sa.DateTime,default=datetime.utcnow)
    )


def downgrade():
    op.drop_table('crypto_transaction')
