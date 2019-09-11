from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Vendor, Customer, Admin, Service, SubService, Status, VendorService, VendorCustomer
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Status)
admin.site.register(VendorService)
admin.site.register(VendorCustomer)
#admin.site.register()
