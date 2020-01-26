from app.server.services.base import BaseService
from app.server.repositories.user import UserRepository
from app.server.models.user import User


class UserService(BaseService):
    def __init__(self,session):
        super(UserService,self).__init__(UserRepository(session,User))

    def insert(self,**sender):
        # here we create our native user 
        # check username not exist
        username_exist = self.repository.get_by_username(sender['username'])
        if username_exist:
            return self.response.failure(message='username exist',status=self.status_code.DUPLICATE)

        # check email not exist
        username_exist = self.repository.get_by_email(sender['email'])
        if username_exist:
            return self.response.failure(message='email exist',status=self.status_code.DUPLICATE)
        # set passwordHash
        # new_kwargs = sender
        sender['password_hash'] = sender['password']
        
        # user = User(**sender)
        # print(user)
        # self.repository.insert(user)
        return self.response.success('ok',None)
        
    
