#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # key = qualified name of the method
        key = method.__qualname__
        # increment the count in Redis
        self._redis.incr(key)
        # call the original method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class to handle Redis operations"""

    def __init__(self):
        """Initialize the Cache with a Redis connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string value from Redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value from Redis"""
        return self.get(key, fn=int)
