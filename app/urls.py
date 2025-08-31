"""
URL configuration for amamentacao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import accounts_view
from login.views import login_view, logout_view
from account_recovery.views import account_recovery_view
from feed.views import feed_view
from settings.views import settings_view
from informations.views import informations_view
from be_a_donor.views import be_a_donor_view
from units.views import units_view
from profiles.views import profiles_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', accounts_view, name='accounts'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('account_recovery/', account_recovery_view, name='account_recovery'),
    path('feed/', feed_view, name='feed'),
    path('settings/', settings_view, name='settings'),
    path('informations/', informations_view, name='informations'),
    path('be_a_donor', be_a_donor_view, name='be_a_donor'),
    path('units', units_view, name='units'),
    path('profiles', profiles_view, name='profiles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para permitir o uso de imagens
