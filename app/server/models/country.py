import sqlalchemy as sa

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base
# from app.server.models.province import Provice

class Country(BaseMixin,Base):
    __tablename__ = 'country'

    id = sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.String,nullable=False)
    # relationship: has many provinces
    provinces = sa.orm.relationship('Province',back_populates='country')

    def __repr__(self):
        return self.id