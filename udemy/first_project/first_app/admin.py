from django.contrib import admin

from .models import Topic, Webpage, AccessRecord, UserProfileModel, user

# Register your models here.

admin.site.register(Topic, user
                    )
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileModel)