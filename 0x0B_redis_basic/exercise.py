#!/usr/bin/env python3
"""Script contains cache class that uses Redis"""
import redis
import uuid
from typing import Union, Callable, Optional, TypeVar, cast
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator that count
    how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Increments the count every time the method is called
        Returns
        - the value returned by the original method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator that stores
    the history of inputs and outputs for a function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Stores input arguments and function output in Redis lists.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


class Cache:
    """Cache class handles caching data using Redis"""

    def __init__(self) -> None:
        # Initialize Redis without decode_responses to get bytes
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method stores data with unique id key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        """
        Retrieve data from Redis and optionally apply a conversion function."""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """
    Display the history of calls of a function.

    Args:
        method: The function whose history to display.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    call_count = redis_instance.get(method_name)
    call_count_int = int(call_count.decode("utf-8")) if call_count else 0

    print(f"{method_name} was called {call_count_int} times:")

    for input_args, output in zip(inputs, outputs):
        input_str = input_args.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")
