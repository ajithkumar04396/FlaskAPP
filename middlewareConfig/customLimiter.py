from app import app
import redis
from configs import config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# :-- Adding redis  --:
pool = redis.connection.BlockingConnectionPool.from_url(config.default['redis']['con'])
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://",
    storage_options={"connection_pool": pool},
    strategy="fixed-window"
)