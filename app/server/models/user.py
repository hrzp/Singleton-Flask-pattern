import sqlalchemy as sa
from datetime import datetime

from app.common.handlers.base_mixin import BaseMixin
from app.common.database import Base

from app.server.models.address import Address
from app.server.models.email_verification_token import EmailVerificationToken
from app.server.models.reset_password_token import ResetPasswordToken

class User(BaseMixin,Base):
    __tablename__ = 'user'
    # def __init__(self,**kwargs):
    #     print('#'*30)
    #     super(User, self).__init__()

    id = sa.Column(sa.Integer,primary_key=True)
    username = sa.Column(sa.String(255),unique=True,nullable=False)
    password_hash = sa.Column(sa.String(255))
    email = sa.Column(sa.String(128))
    name = sa.Column(sa.String())
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    last_login = sa.Column(sa.DateTime)
    # relationship: has many addresses
    address_id = sa.Column(sa.Integer,sa.ForeignKey('address.id'))
    address = sa.orm.relationship('Address')
    email_verified = sa.Column(sa.Boolean,default=False)
    email_verification_token = sa.orm.relationship('EmailVerificationToken',uselist=False,back_populates="user")
    reset_password_tokens = sa.orm.relationship('ResetPasswordToken',back_populates="user")

    def __repr__(self):
        return str(self.id) or ""