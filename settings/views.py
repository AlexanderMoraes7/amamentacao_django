from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def settings_view(request : HttpRequest):
    return render(
        request,
        'settings.html',
    )