from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def profiles_view(request : HttpRequest):
    return render(
        request,
        'profiles.html',
    )