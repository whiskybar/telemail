from django import forms
from django.contrib import admin
from telemail.addresses.models import Account, Alias, Forward


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {
                'password': forms.PasswordInput(render_value=False),
        }
        
class AccountAdmin(admin.ModelAdmin):
    form = AccountForm
    search_fields = ['address']

admin.site.register(Account, AccountAdmin)


class AliasAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination')
    search_fields = ['source', 'destination']

admin.site.register(Alias, AliasAdmin)


class ForwardAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination')
    search_fields = ['source', 'destination']

admin.site.register(Forward, ForwardAdmin)
