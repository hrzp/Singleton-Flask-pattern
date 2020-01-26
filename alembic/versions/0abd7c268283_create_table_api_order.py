"""create table api_order

Revision ID: 0abd7c268283
Revises: 194e8aedb1d5
Create Date: 2019-11-03 12:45:38.443354

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '0abd7c268283'
down_revision = '194e8aedb1d5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'api_order',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('terminal_id',sa.Integer,sa.ForeignKey('terminal.id')),
        sa.Column('request_date_time',sa.DateTime,default=datetime.utcnow),
        sa.Column('cryptocurrency_id',sa.Integer,sa.ForeignKey('cryptocurrency.id')),
        sa.Column('amount',sa.Float,nullable=False),
        sa.Column('order_id',sa.String,nullable=False),
        sa.Column('hook_url',sa.String,nullable=False),
        sa.Column('wallet_id',sa.Integer,sa.ForeignKey('wallet.id'))
    )


def downgrade():
    op.drop_table('api_order')
