"""create table address

Revision ID: f65251d23390
Revises: b62d92e5afdd
Create Date: 2019-10-24 12:45:07.768874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f65251d23390'
down_revision = 'b62d92e5afdd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('city_id',sa.Integer,sa.ForeignKey('city.id')),
        sa.Column('address_line',sa.String),
        sa.Column('zip_code',sa.String(64)),
        sa.Column('postal_code',sa.String(64))
    )


def downgrade():
    op.drop_table('address')