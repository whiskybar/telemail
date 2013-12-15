from django.contrib import admin
from spam.models import NoSpamHost, NoSpamRecipient


class NoSpamHostAdmin(admin.ModelAdmin):
    search_fields = ['host']
        
admin.site.register(NoSpamHost, NoSpamHostAdmin)


class NoSpamRecipientAdmin(admin.ModelAdmin):
    search_fields = ['address']
        
admin.site.register(NoSpamRecipient, NoSpamRecipientAdmin)
        
