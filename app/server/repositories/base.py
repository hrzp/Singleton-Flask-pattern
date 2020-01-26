class BaseRepository:
    def __init__(self,db_session,entity):
        self.db_session = db_session
        self.entity = entity
    
    def get_all(self):
        return self.db_session.query(self.entity).all()
    
    def get_first(self):
        return self.db_session.query(self.entity).first()
    
    def find_by_id(self,id):
        pass

    def delete_by_id(self,id):
        pass

    def update(self,entity):
        pass

    def insert(self,entity):
        self.db_session.add(entity)
        self.db_session.commit()
        return entity
    
