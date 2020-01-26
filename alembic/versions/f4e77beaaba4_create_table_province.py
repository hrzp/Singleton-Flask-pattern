"""create table province

Revision ID: f4e77beaaba4
Revises: 0f931b54fbbf
Create Date: 2019-10-24 12:44:51.663435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e77beaaba4'
down_revision = '0f931b54fbbf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'province',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('name',sa.String(64),nullable=False),
        sa.Column('country_id',sa.Integer,sa.ForeignKey('country.id'))
    )


def downgrade():
    op.drop_table('province')
