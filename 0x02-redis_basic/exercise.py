#!/usr/bin/env python3
"""redies exercise"""
import redis
import uuid
from typing import Union, Callable
import functools



def count_calls(methode: Callable) -> Callable:
    """decorater funcction to count how many cach class is call"""
    @functools.wraps(methode)
    def wrapper(self, *args, **kwargs):
        """increase the value of count"""
        self._redis.incr(methode.__qualname__)
        return methode(self, *args, **kwargs)
    return wrapper

class Cache():
    """cache class"""

    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, float, int, bytes]) -> str:
        """store data with specific id"""
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key: str, fn: Union[Callable, None]=None) -> Union[str, bytes, float, int]:
        """get data from redis and conver thee byte to data"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """implement get str with get method"""
        str_data = self.get(key, lambda x: x.decode('utf-8'))
        return str_data        

    def get_int(self, key: str) -> int:
        """implement get int with get method"""
        int_data = self.get(key, int())
        return int_data
