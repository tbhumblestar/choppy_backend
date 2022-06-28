from django.contrib import admin
from .models import SupportCompany,Album
from django.contrib.auth.models import Group

admin.site.register(SupportCompany)
admin.site.register(Album)
admin.site.unregister(Group)