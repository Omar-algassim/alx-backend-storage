#!/usr/bin/env python3
"""redies exercise"""
import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(methode: Callable) -> Callable:
    """decorater funcction to count how many cach class is call"""
    @functools.wraps(methode)
    def wrapper(self, *args, **kwargs) -> Any:
        """increase the value of count"""
        self._redis.incr(methode.__qualname__)
        return methode(self, *args, **kwargs)
    return wrapper


def call_history(methode: Callable) -> Callable:
    """methode save the output and input in list"""
    @functools.wraps(methode)
    def wrapper(self, *args, **kwargs):
        """wrapper for decarator"""
        out_key = f"{methode.__qualname__}:outputs"
        in_key = f"{methode.__qualname__}:inputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = methode(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return wrapper


def replay(method):
    """replay with information about call history"""
    redis_ = getattr(method.__self__, "_redis", None)
    call_num = redis_.get(method.__qualname__)
    input_list = redis_.lrange(f"{method.__qualname__}:inputs", 0, -1)
    output_list = redis_.lrange(f"{method.__qualname__}:outputs", 0, -1)
    print(f"{method.__name__} was called {int(call_num)} times:")
    for inp, outp in zip(input_list, output_list):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) ->\
            {outp.decode('utf-8')}")


class Cache():
    """cache class"""

    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, float, int, bytes]) -> str:
        """store data with specific id"""
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key: str,
            fn: Union[Callable, None] = None
            ) -> Union[str, bytes, float, int]:
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
