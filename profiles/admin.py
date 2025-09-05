from django.contrib import admin
from .models import Photo, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_address', 'user__username', 'get_user_email')

    def get_user_email(self, obj):
        return obj.user.email


admin.site.register(Address, AddressAdmin)
admin.site.register(Photo)
