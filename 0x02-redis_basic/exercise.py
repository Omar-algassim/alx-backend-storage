#!/usr/bin/env python3
"""redies exercise"""
import redis
import uuid
from typing import Union, Callable

class Cache():
    """cache class"""
    
    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    
    def store(self, data: Union[str, float, int, bytes]) -> str:
        """store data with specific id"""
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key: str, fn: Union[Callable, None]) -> Union[str, bytes, float, int]:
        """get data from redis and conver thee byte to data"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """implement get str with get method"""
        str_data = self.get(data, str())
        return str_data        
    
    def get_int(self, data: bytes) -> int:
        """implement get int with get method"""
        int_data = self.get(data, int())
        return int_data
