from django.contrib import admin

from .models import User, ActivationCode


admin.site.register(User)
admin.site.register(ActivationCode)
