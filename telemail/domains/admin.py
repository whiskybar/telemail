from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from telemail.domains.models import DomainTrash


class DomainTrashAdmin(admin.ModelAdmin):
    list_display = ('domain', 'trash')
    search_fields = ['domain', 'trash']

admin.site.register(DomainTrash, DomainTrashAdmin)

admin.site.unregister(Group)
