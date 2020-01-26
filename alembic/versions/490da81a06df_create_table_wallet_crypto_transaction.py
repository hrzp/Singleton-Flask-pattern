"""create table wallet_crypto_transaction

Revision ID: 490da81a06df
Revises: ffb5c6ec63ff
Create Date: 2019-11-02 16:59:44.875768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490da81a06df'
down_revision = 'ffb5c6ec63ff'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wallet_crypto_transaction',
        sa.Column('wallet_id',sa.Integer,sa.ForeignKey('wallet.id')),
        sa.Column('crypto_transaction_id',sa.Integer,sa.ForeignKey('crypto_transaction.id'))
    )


def downgrade():
    op.drop_table('wallet_crypto_transaction')
