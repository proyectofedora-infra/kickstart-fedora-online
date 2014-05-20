# -*- coding: utf-8 -*-
from functools import wraps


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not has_admin():
            return "You don't have permission"
        return f(*args, **kwargs)
    return wrapper
