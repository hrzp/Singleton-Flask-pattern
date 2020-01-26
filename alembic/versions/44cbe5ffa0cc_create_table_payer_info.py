"""create_table_payer_info

Revision ID: 44cbe5ffa0cc
Revises: d6af8205d0fb
Create Date: 2019-11-02 17:43:57.875034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44cbe5ffa0cc'
down_revision = 'd6af8205d0fb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'payer_info',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('email',sa.String),
        sa.Column('mobile_number',sa.String(20))
    )


def downgrade():
    op.drop_table('payer_info')
