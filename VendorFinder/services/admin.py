from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    User,
    Vendor,
    Customer,
    Admin,
    Service,
    SubService,
    Status,
    VendorService,
    Invoice
)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Status)
admin.site.register(VendorService)
admin.site.register(Invoice)
#admin.site.register()