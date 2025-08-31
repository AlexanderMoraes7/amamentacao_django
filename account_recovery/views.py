from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def account_recovery_view(request):
    return render(
        request,
        'account_recovery.html',
    )