import sqlalchemy as sa
from app.common.handlers.base_mixin import BaseMixin

from app.common.database import Base
from app.server.models.city import City

class Address(BaseMixin,Base):
    __tablename__ = 'address'

    id = sa.Column(sa.Integer,primary_key=True)
    address_line = sa.Column(sa.String)
    zip_code = sa.Column(sa.String(64))
    postal_code = sa.Column(sa.String(64))
    # relationship: has one city
    city_id = sa.Column(sa.Integer,sa.ForeignKey('city.id'))
    city = sa.orm.relationship('City')

    def __repr__(self):
        return self.id
    