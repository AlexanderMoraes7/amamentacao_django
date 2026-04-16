from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def be_a_donor_view(request : HttpRequest):
    return render(
        request,
        'be_a_donor.html',
    )