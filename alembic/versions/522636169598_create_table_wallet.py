"""create table wallet

Revision ID: 522636169598
Revises: 4e220556c0e2
Create Date: 2019-11-02 15:34:17.736079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '522636169598'
down_revision = '4e220556c0e2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wallet',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('cryptocurrency_id',sa.Integer,sa.ForeignKey('cryptocurrency.id')),
        sa.Column('private_key',sa.String(256),nullable=False,unique=True),
        sa.Column('address',sa.String(128),nullable=False,unique=True),
        sa.Column('type',sa.SmallInteger),
        sa.Column('balance',sa.Float,nullable=False,default=0)
    )


def downgrade():
    op.drop_table('wallet')
