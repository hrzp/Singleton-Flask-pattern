"""create table seller

Revision ID: 09a68103be36
Revises: 21a398f4b70c
Create Date: 2019-10-24 16:44:30.367676

"""
from alembic import op
import sqlalchemy as sa
import enum

# revision identifiers, used by Alembic.
revision = '09a68103be36'
down_revision = '21a398f4b70c'
branch_labels = None
depends_on = None

class BusinessTypeEnum(enum.Enum):
    personal = 0
    another = 1

def upgrade():
    op.create_table(
        'seller',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('user_id',sa.Integer,sa.ForeignKey('user.id')),
        sa.Column('business_type',sa.Enum(BusinessTypeEnum),nullable=False)
    )


def downgrade():
    op.drop_table('seller')
    sa.Enum(name='businesstypeenum').drop(op.get_bind(), checkfirst=False)
