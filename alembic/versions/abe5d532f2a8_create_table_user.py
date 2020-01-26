"""create table user

Revision ID: abe5d532f2a8
Revises: f65251d23390
Create Date: 2019-10-24 12:45:34.611207

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'abe5d532f2a8'
down_revision = 'f65251d23390'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('username',sa.String(255),unique=True,nullable=False),
        sa.Column('password_hash',sa.String(255)),
        sa.Column('email',sa.String(128)),
        sa.Column('name',sa.String()),
        sa.Column('address_id',sa.Integer,sa.ForeignKey('address.id')),
        sa.Column('created_at',sa.DateTime, default=datetime.utcnow),
        sa.Column('last_login',sa.DateTime),
        sa.Column('is_active',sa.Boolean,default=True),
        sa.Column('email_verified',sa.Boolean,default=False)
    )


def downgrade():
    op.drop_table('user')
