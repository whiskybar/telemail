from django import forms
from django.contrib import admin
from addresses.models import Account


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
