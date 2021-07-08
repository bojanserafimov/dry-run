"""Module for declaring trouble and guarding against it.

Currently single-threaded.

TODO make it somewhat thread-safe. Approaches:
i) Make STACK thread-local
ii) Put STACK in the stack, find it with inspect module
iii) Use lock file, or maybe etcd lock

"""
import inspect

class PossibleTrouble(Exception):
    """Raise when function was not expected to be called."""

STACK = []


def cause(func):
    def decorated(*args, **kwargs):
        for safe in STACK:
            if not safe(decorated, args, kwargs):
                raise PossibleTrouble()
        return func(*args, **kwargs)
    decorated.__signature__ = inspect.signature(func)
    return decorated


def expected(safety_predicate):
    def decorator(func):
        def decorated(*args, **kwargs):
            STACK.append(safety_predicate)
            try:
                return func(*args, **kwargs)
            finally:
                assert STACK.pop() == safety_predicate
        decorated.__signature__ = inspect.signature(func)
        return decorated
    return decorator


def no_trouble(token, args, kwargs):
    return False
