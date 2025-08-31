from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm

@login_required(redirect_field_name='login')
def profiles_view(request : HttpRequest):
    # Tenta pegar o objeto Photo do usuário. Se não existir, cria um novo.
    photo_obj, created = Photo.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Passa a instância existente para o formulário para que ele a atualize
        form = PhotoForm(request.POST, request.FILES, instance=photo_obj)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    else:
        form = PhotoForm(instance=photo_obj)

    context = {
        'form': form
    }
    return render(request, 'profiles.html', context)
