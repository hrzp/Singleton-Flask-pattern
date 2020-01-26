from flask import Blueprint
from app.server.services.user import UserService
from app.common.database import db_session
from webargs.flaskparser import use_args
from app.server.validations.register_user import register_user_args
from app.server.validations.login import login_args

user = Blueprint('user',__name__)
user_service = UserService(db_session)


@user.route('/register',methods=['POST'])
@use_args(register_user_args)
def register(request):
    result = user_service.insert(**request)
    return result


@user.route('/login',methods=['POST'])
@use_args(login_args)
def login():
    # lets create user
    return 'login'


@user.route('/home',methods=['GET'])
def home():
    user = User(username="armani",password_hash="123456",email="arman@arman.com",name="Arman Hoseini")
    result = user_service.insert(user)
    return result
