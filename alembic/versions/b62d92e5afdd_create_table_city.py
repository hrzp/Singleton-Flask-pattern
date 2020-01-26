"""create table city

Revision ID: b62d92e5afdd
Revises: f4e77beaaba4
Create Date: 2019-10-24 12:44:58.974268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b62d92e5afdd'
down_revision = 'f4e77beaaba4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'city',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String(64),nullable=False),
        sa.Column('province_id',sa.Integer,sa.ForeignKey('province.id'))
    )


def downgrade():
    op.drop_table('city')
