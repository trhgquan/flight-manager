from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    '''Redirect user to home page 
    if they are logged in and accessing to non-logged-in routes.'''
    
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        return view_function(request, *args, **kwargs)
    
    return wrapper_function