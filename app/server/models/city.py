import sqlalchemy as sa

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base

from app.server.models.province import Province

class City(BaseMixin,Base):
    __tablename__ = 'city'

    id = sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.String(64),nullable=False)
    # relationship: belongs to one province
    province_id = sa.Column(sa.Integer,sa.ForeignKey('province.id'))
    province = sa.orm.relationship('Province',back_populates='cities')

    def __repr__(self):
        return self.id