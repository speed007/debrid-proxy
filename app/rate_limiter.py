from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    storage_uri="redis://redis:6379",  # Uses Redis
    default_limits=["30 per minute"]
)
