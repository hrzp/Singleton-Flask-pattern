"""create table seller_withdraw_request

Revision ID: ec4391665eeb
Revises: 0abd7c268283
Create Date: 2019-11-03 13:03:22.137139

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'ec4391665eeb'
down_revision = '0abd7c268283'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'seller_withdraw_request',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('amount',sa.Float,nullable=False),
        sa.Column('options',sa.JSON),
        sa.Column('destination_address',sa.String(128),nullable=False),
        sa.Column('seller_approve',sa.Boolean,default=False),
        sa.Column('status',sa.SmallInteger),
        sa.Column('crypto_transaction_id',sa.Integer,sa.ForeignKey('crypto_transaction.id')),
        sa.Column('created_at',sa.DateTime,default=datetime.utcnow)
    )


def downgrade():
    op.drop_table('seller_withdraw_request')
