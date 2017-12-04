"""Methods for admin authentication"""
from functools import wraps
from flask import request, Response

#This function is used to check that the user's username and password
#match the admin username and password.
def are_credentials_correct(username, password):
    """Returns True if the given password matches the Admin password,
    and the given username matches the admin username."""
    return password == "drKH5$7Yy^!aSa7UHGydj8zAieeB6ayv" and username == "admin"

#This function is used to allow the user to login if they are not already,
#or their credentials are incorrect.
def login():
    """Sends a 401 response that enables basic auth"""
    #Responds to the client. The header attribute, 'WWW-Authenticate':'Basic realm="Login Required",
    #tells the client browser that authentication is required, prompting the user to login.
    #Error code 401 means Forbidden. The body of the response is 'Please enter admin credentials.'
    return Response(
        'Please enter admin credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

#Decorator function for route methods.
#When added to routes, this funcion makes the route depend on admin authorization.
#I'm not very familiar with decorator funtions, there may be ways to improve this.
#Perhaps by depending on the route decorator somehow, and logging an error if not found.
def requires_admin(method):
    """When added to a route function, this decorator makes the route
    require admin authentication."""
    @wraps(method)
    def decorated(*args, **kwargs): #Keep decorated function arguments and keyword arguments.
        auth = request.authorization #username & password in the request header.
        #if no username & password was found, or the username & password are wrong...
        if not auth or not are_credentials_correct(auth.username, auth.password):
            return login() #Prompt the user to login.
        #Return the wrapped route method.
        return method(*args, **kwargs)
    return decorated
