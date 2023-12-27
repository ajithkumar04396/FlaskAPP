from app import app
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = config.default['JWT']['JWT_SECRET_KEY']
JWTManager(app)