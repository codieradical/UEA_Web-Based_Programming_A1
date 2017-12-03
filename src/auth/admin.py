"""Methods for admin authentication"""
from functools import wraps
from flask import request, Response

def are_credentials_correct(username, password):
    """Returns True if the given password matches the Admin password,
    and the given username matches the admin username."""
    return password == "drKH5$7Yy^!aSa7UHGydj8zAieeB6ayv" and username == "admin"

def login():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Please enter admin credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_admin(method):
    """When added to a route function, this decorator makes the route
    require admin authentication."""
    @wraps(method)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not are_credentials_correct(auth.username, auth.password):
            return login()
        return method(*args, **kwargs)
    return decorated
