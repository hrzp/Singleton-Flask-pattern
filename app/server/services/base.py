from app.common.handlers.response import Response
from app.common.variables.enums import STATUS_CODES
import time
class BaseService:
    def __init__(self,repository):
        self.repository = repository
        self.response = Response
        self.status_code = STATUS_CODES
        
    
    def get_all(self):
        # result = [user.json() for user in self.repository.get_all()]
        result = self.repository.get_first()
        
        if not result:
            return self.response.failure('Item not Found',status=self.status_code.NOT_FOUND)
        return self.response.success('Ok',result.json())