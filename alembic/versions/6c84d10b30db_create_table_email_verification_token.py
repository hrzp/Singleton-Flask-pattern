"""create table email_verification_token

Revision ID: 6c84d10b30db
Revises: ef0df4302c6a
Create Date: 2019-11-09 15:14:25.182563

"""
from alembic import op
import sqlalchemy as sa

from datetime import datetime


# revision identifiers, used by Alembic.
revision = '6c84d10b30db'
down_revision = 'ef0df4302c6a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'email_verification_token',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('token',sa.String(64),unique=True,nullable=False),
        sa.Column('user_id',sa.Integer,sa.ForeignKey('user.id')),
        sa.Column('created_at',sa.DateTime,default=datetime.utcnow),
    )


def downgrade():
    op.drop_table('email_verification_token')
