"""create table terminal_order_wallet

Revision ID: 194e8aedb1d5
Revises: 3c4c3f3261d1
Create Date: 2019-11-02 17:48:58.687110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194e8aedb1d5'
down_revision = '3c4c3f3261d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'terminal_order_wallet',
        sa.Column('terminal_order_id',sa.Integer,sa.ForeignKey('terminal_order.id')),
        sa.Column('wallet_id',sa.Integer,sa.ForeignKey('wallet.id')),
        sa.Column('amount',sa.Float,nullable=False)
    )


def downgrade():
    op.drop_table('terminal_order_wallet')
