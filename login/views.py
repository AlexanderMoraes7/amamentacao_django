from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST

def login_view(request : HttpRequest):
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('feed')
        else:
            login_form = (AuthenticationForm(request, data=request.POST))
    else:
        login_form = AuthenticationForm()
    
    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')