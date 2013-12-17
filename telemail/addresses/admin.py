from django import forms
from django.contrib import admin
from telemail.addresses.models import Account, Alias, Forward, ForwardedAddress


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


class ForwardedAddressInline(admin.TabularInline):
    model = ForwardedAddress
    verbose_name = 'address'
    verbose_name_plural = 'forward to'

class ForwardAdmin(admin.ModelAdmin):
    list_display = ('address', 'forward_to')
    search_fields = ['address', 'destinations__destination']
    
    def forward_to(self, obj):
        return ', '.join(d.destination for d in obj.destinations.all())
    forward_to.short_description = 'forward to'
    
    inlines = [ForwardedAddressInline]

admin.site.register(Forward, ForwardAdmin)
