from app.server.repositories.base import BaseRepository
class UserRepository(BaseRepository):
    def get_by_username(self,username):
        return self.db_session.query(self.entity).filter_by(username=username).first()

    def get_by_email(self,email):
        return self.db_session.query(self.entity).filter_by(email=email).first()