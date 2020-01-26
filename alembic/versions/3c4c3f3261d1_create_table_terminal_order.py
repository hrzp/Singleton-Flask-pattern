"""create table terminal_order

Revision ID: 3c4c3f3261d1
Revises: 44cbe5ffa0cc
Create Date: 2019-11-02 17:46:12.281188

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '3c4c3f3261d1'
down_revision = '44cbe5ffa0cc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'terminal_order',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('terminal_id',sa.Integer,sa.ForeignKey('terminal.id')),
        sa.Column('request_date_time',sa.DateTime,default=datetime.utcnow),
        sa.Column('default_cryptocurrency_id',sa.Integer,sa.ForeignKey('cryptocurrency.id')),
        sa.Column('base_amount',sa.Float,nullable=False),
        sa.Column('callback_url',sa.String),
        sa.Column('hook_url',sa.String),
        sa.Column('order_id',sa.String,nullable=False),
        sa.Column('status',sa.SmallInteger),
        sa.Column('token',sa.String,nullable=False),
        sa.Column('description',sa.String),
        sa.Column('open_gateway_datetime',sa.DateTime),
        sa.Column('chosen_wallet_id',sa.Integer,sa.ForeignKey('wallet.id')),
        sa.Column('chosen_crypto_amount',sa.Float),
        sa.Column('payer_info_id',sa.Integer,sa.ForeignKey('payer_info.id'))
    )


def downgrade():
    op.drop_table('terminal_order')
