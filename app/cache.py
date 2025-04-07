import redis
from functools import wraps
import pickle
import os
from datetime import timedelta

# Initialize Redis connection
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=False
)

def cache_response(ttl: int = 3600):
    """Decorator to cache function responses in Redis."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate unique cache key
            cache_key = f"cache:{func.__module__}:{func.__name__}:{args}:{kwargs}"
            
            # Try to get cached result
            cached = redis_client.get(cache_key)
            if cached:
                return pickle.loads(cached)
            
            # Execute function if not cached
            result = func(*args, **kwargs)
            
            # Store result with TTL
            redis_client.setex(
                name=cache_key,
                time=timedelta(seconds=ttl),
                value=pickle.dumps(result)
            )
            return result
        return wrapper
    return decorator

def clear_cache(pattern: str = "cache:*"):
    """Clear all or specific cached entries."""
    for key in redis_client.scan_iter(match=pattern):
        redis_client.delete(key)
