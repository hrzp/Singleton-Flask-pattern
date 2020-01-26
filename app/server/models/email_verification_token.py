import sqlalchemy as sa
from datetime import datetime

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base

class EmailVerificationToken(BaseMixin,Base):
    __tablename__ = "email_verification_token"

    id = sa.Column(sa.Integer,primary_key=True)
    token = sa.Column(sa.String(64),unique=True,nullable=False)
    created_at = sa.Column(sa.DateTime,default=datetime.utcnow)
    
    user_id = sa.Column(sa.Integer,sa.ForeignKey('user.id'))
    user = sa.orm.relationship('User',back_populates='email_verification_token')
    

    def __repr__(self):
        return self.id