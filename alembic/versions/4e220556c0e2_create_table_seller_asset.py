"""create table seller_asset

Revision ID: 4e220556c0e2
Revises: 09a68103be36
Create Date: 2019-11-02 14:36:01.583724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e220556c0e2'
down_revision = '09a68103be36'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'seller_asset',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('seller_id',sa.Integer,sa.ForeignKey('seller.id')),
        sa.Column('cryptocurrency_id',sa.Integer,sa.ForeignKey('cryptocurrency.id')),
        sa.Column('amount',sa.Float,default=0,nullable=False)
    )


def downgrade():
    op.drop_table('seller_asset')
