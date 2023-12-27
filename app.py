from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_validate_json import validate_json
from configs import config
import logging
import os


#  :-- Default flaskApp configurations --:
# :-- Adding logger to flaskApp at root directory. --:
logging.basicConfig(filename=config.default['flaskAppDefault']['logger'], level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# :-- Initializing the flasApp --:
app = Flask(__name__)
app.config.from_object(__name__)

# :-- Adding middleware for URL and Hyperlinks fields for HATEOAS-ready APIs --:
ma = Marshmallow(app)

# :-- Adding middleware for handling Cross Origin Resource Sharing (CORS) --:
CORS(app,
  resources={r'/*': {"origins": '*'}},
  supports_credentials=True
)

# :-- Adding middleware bcrypt --:
bcrypt = Bcrypt(app)

#  :-- End default flaskApp configurations --:

#  :-- Custom flaskApp configurations --:
# :-- Adding custom config to flaskApp --:
# app.config['HOSTED_PATH']=os.getenv(os.environ["FLASK_APP"],None)

# :-- Adding secrect key to flaskApp --:
app.secret_key=config.default['flaskAppDefault']['secretKey']

from middlewareConfig.customLimiter import limiter
from exception import validationHttpExceptionHandler
# :-- Configuring blueprints --:
from view.view import view
from restApi.restApi import restApi
app.register_blueprint(view)
app.register_blueprint(restApi)

if __name__ == '__main__':
  app.run()