"""create table reset_password_token

Revision ID: 8a5c0b540583
Revises: 6c84d10b30db
Create Date: 2019-11-09 15:14:52.709851

"""
from alembic import op
import sqlalchemy as sa

from datetime import datetime


# revision identifiers, used by Alembic.
revision = '8a5c0b540583'
down_revision = '6c84d10b30db'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reset_password_token',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('token',sa.String,unique=True,nullable=False),
        sa.Column('user_id',sa.Integer,sa.ForeignKey('user.id')),
        sa.Column('created_at',sa.DateTime,default=datetime.utcnow),
        sa.Column('expire_date',sa.DateTime,nullable=False)
    )


def downgrade():
    op.drop_table('reset_password_token')
