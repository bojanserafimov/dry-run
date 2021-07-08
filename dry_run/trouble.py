"""Module for declaring trouble and guarding against it.

Currently single-threaded.

TODO make it somewhat thread-safe. Approaches:
i) Make STACK thread-local
ii) Put STACK in the stack, find it with inspect module

TODO add type hints and input validation

TODO test that these decorators preserve function
metadata and type signature.

TODO set up github CI, test in multiple python versions
"""


class PossibleTrouble(Exception):
    def __init__(self, trouble_token):
        self.trouble_token = trouble_token

STACK = []

def could_cause(trouble_token):
    def decorator(func):
        def decorated(*args, **kwargs):
            for safety_predicate in STACK:
                if not safety_predicate(trouble_token):
                    raise PossibleTrouble(trouble_token)
            return func(*args, **kwargs)
        return decorated
    return decorator


def could_only_cause(safety_predicate):
    def decorator(func):
        def decorated(*args, **kwargs):
            STACK.append(safety_predicate)
            try:
                return func(*args, **kwargs)
            finally:
                assert STACK.pop() == safety_predicate
        return decorated
    return decorator


nothing = lambda x: False

def only(thing):
    return lambda t : t == thing

def one_of(things):
    return lambda t : t in things
