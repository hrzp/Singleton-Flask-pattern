"""create table seller_withdraw_transaction

Revision ID: ef0df4302c6a
Revises: ec4391665eeb
Create Date: 2019-11-03 13:13:15.366448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef0df4302c6a'
down_revision = 'ec4391665eeb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'seller_withdraw_transaction',
        sa.Column('seller_withdraw_request_id',sa.Integer,sa.ForeignKey('seller_withdraw_request.id')),
        sa.Column('wallet_id',sa.Integer,sa.ForeignKey('wallet.id'))
    )


def downgrade():
    op.drop_table('seller_withdraw_transaction')
