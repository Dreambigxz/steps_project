from django.contrib import admin
from .models import Capital, Unpaid_user, Paid_user, PTransaction

# Register your models here.
admin.site.register(Capital)
admin.site.register(Unpaid_user)
admin.site.register(Paid_user)
admin.site.register(PTransaction)