from django.contrib import admin
from telemail.spam.models import NoSpamHost, NoSpamRecipient, Subject


class NoSpamHostAdmin(admin.ModelAdmin):
    search_fields = ['host']
        
admin.site.register(NoSpamHost, NoSpamHostAdmin)


class NoSpamRecipientAdmin(admin.ModelAdmin):
    search_fields = ['address']
        
admin.site.register(NoSpamRecipient, NoSpamRecipientAdmin)


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['subject']
        
admin.site.register(Subject, SubjectAdmin)
        
