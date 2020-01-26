from flask import Flask,g
import logging
import app.config.conf
from app.common.handlers.response import Response

response = Response()

app = Flask(__name__)

app.secret_key = "Something_from_config"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



# TODO: Write and handle errors by an ErrorHandler 


@app.errorhandler(422)
def validation_error(error):
    result = response.failure('validation error',error.data['messages'],422)
    return result,200

try:
    import app.server.routes as api
    api.register_blueprints(app)
except Exception as e:
    print(e)

