from django.contrib import admin
from telemail.domains.models import DomainTrash


class DomainTrashAdmin(admin.ModelAdmin):
    list_display = ('domain', 'trash')
    search_fields = ['domain', 'trash']

admin.site.register(DomainTrash, DomainTrashAdmin)
