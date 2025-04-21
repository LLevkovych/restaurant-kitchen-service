from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import Cook

admin.site.register(Cook, UserAdmin)
