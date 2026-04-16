from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def account_recovery_view(request):
    return render(
        request,
        'account_recovery.html',
    )