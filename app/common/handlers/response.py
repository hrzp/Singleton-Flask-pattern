from flask import jsonify

class Response:
    @staticmethod
    def success(message = None,payload = None):
        return jsonify({
            "isSuccessful":True,
            "payload":payload,
            "status":200,
            "message":message
        })
    
    @staticmethod
    def failure(message = None,errors = [],status=0):
        return jsonify({
            "isSuccessful":False,
            "errors":errors,
            "status":status,
            "message":message
        })
