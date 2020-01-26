import sqlalchemy as sa

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base

from app.server.models.country import Country

class Province(BaseMixin,Base):
    __tablename__ = 'province'

    id = sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.String(64),nullable=False)
    # relationship: belongs to one country
    country_id = sa.Column(sa.Integer,sa.ForeignKey('country.id'))
    country = sa.orm.relationship('Country',back_populates='provinces')
    # relationship: has many cities
    cities = sa.orm.relationship('City',back_populates='province')

    def __repr__(self):
        return self.id