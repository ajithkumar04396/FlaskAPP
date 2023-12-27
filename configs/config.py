from configs import environ

default = {
    "flaskAppDefault": {
        "logger": 'flaskApplogs.log',
        "secretKey": 'FlaskAppSecrectKeyCodingSimple'
    },
    "redis": {
        "con": environ.REDIS_HOST
    },
    "JWT":{
        "JWT_SECRET_KEY": 'FlaskAppJWTSecrectKeyCodingSimple'
    }
}