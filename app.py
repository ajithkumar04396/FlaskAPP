from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import logging
import os

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
app.config.from_object(__name__)
# app.config['HOSTED_PATH']=os.getenv(os.environ["FLASK_APP"],None)
app.secret_key="FlaskAppSecrectKeyIamJocker"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
# db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
bcrypt = Bcrypt(app)


from view.view import view
app.register_blueprint(view)

if __name__ == '__main__':
  app.run()