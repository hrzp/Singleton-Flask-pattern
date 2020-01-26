import sqlalchemy as sa
from datetime import datetime

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base

class ResetPasswordToken(BaseMixin,Base):
    __tablename__ = 'reset_password_token'

    id = sa.Column(sa.Integer,primary_key=True)
    token = sa.Column(sa.String(64),unique=True,nullable=False)
    create_at = sa.Column(sa.DateTime,default=datetime.utcnow)
    expire_date = sa.Column(sa.DateTime,nullable=False)

    user_id = sa.Column(sa.Integer,sa.ForeignKey('user.id'))
    user = sa.orm.relationship('User',back_populates='reset_password_tokens')

    def __repr__(self):
        return self.id