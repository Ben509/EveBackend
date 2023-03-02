from flask import session
from functools import wraps


def needs_auth():
    def _needs_auth(f):
        @wraps(f)
        def __needs_auth(*args, **kwargs):
            if "email" not in session:
                return "", 401
            result = f(*args, **kwargs)
            return result

        return __needs_auth

    return _needs_auth
