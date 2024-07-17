#!/usr/bin/env python3
"""redies exercise"""
import redis
import uuid
from typing import Union

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
