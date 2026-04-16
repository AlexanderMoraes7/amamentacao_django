from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import AccountsForm
from django.contrib import messages

def accounts_view(request : HttpRequest):
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
    else:
        form = AccountsForm()

    return render(
        request,
        'accounts.html',
        {'accounts_form': form}
    )