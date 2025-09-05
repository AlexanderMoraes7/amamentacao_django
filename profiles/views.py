from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Photo, Address
from .forms import PhotoForm, ProfilesForm, AddressForm


@login_required(redirect_field_name='login')
def profiles_view(request : HttpRequest):
    photo_obj, _ = Photo.objects.get_or_create(user=request.user)
    address_obj, _ = Address.objects.get_or_create(user=request.user)
    user_obj = request.user

    if request.method == 'POST':
        # O campo 'path_image' só estará em request.FILES se for o form da foto
        if 'path_image' in request.FILES:
            photo_form = PhotoForm(request.POST, request.FILES, instance=photo_obj)
            if photo_form.is_valid():
                photo_form.save()
                return redirect('profiles')
            
        # Verifica se o formulário de PERFIL foi submetido (pelo botão 'update_profile')
        if 'update_profile' in request.POST:
            user_form = ProfilesForm(request.POST, instance=user_obj)
            address_form = AddressForm(request.POST, instance=address_obj)
            if user_form.is_valid() and address_form.is_valid():
                user_form.save()
                address_form.save()
                return redirect('profiles')
    else:
        photo_form = PhotoForm(instance=photo_obj)
        user_form = ProfilesForm(instance=user_obj)
        address_form = AddressForm(instance=address_obj)

    context = {
        'photo_form': photo_form,
        'user_form': user_form,
        'address_form': address_form,
    }
    return render(request, 'profiles.html', context)
