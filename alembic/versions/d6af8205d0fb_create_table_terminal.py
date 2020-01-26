"""create table terminal

Revision ID: d6af8205d0fb
Revises: 490da81a06df
Create Date: 2019-11-02 17:28:52.844441

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'd6af8205d0fb'
down_revision = '490da81a06df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'terminal',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('seller_id',sa.Integer,sa.ForeignKey('seller.id')),
        sa.Column('valid_ip',sa.String(15),nullable=False),
        sa.Column('request_limit_per_hour',sa.SmallInteger),
        sa.Column('secret_key',sa.String(36),unique=True,nullable=False),
        sa.Column('created_at',sa.DateTime,default=datetime.utcnow)
    )


def downgrade():
    op.drop_table('terminal')
