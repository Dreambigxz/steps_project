from django.contrib import admin
from .models import MyUser
from .forms import UserAdmin
# Register your models here.
admin.site.register(MyUser, UserAdmin)
# Register your models here.
