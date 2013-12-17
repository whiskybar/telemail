from django import forms
from django.contrib import admin
from telemail.addresses.models import Account, Alias, Other, Forward, ForwardedAddress


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


class OtherInline(admin.TabularInline):
    model = Other
    verbose_name = 'alias'
    verbose_name_plural = 'aliases'

class AliasAdmin(admin.ModelAdmin):
    list_display = ('address', 'others')
    search_fields = ['address', 'aliases_alias']

    def others(self, obj):
        return ', '.join(d.alias for d in obj.aliases.all())
    others.short_description = 'aliases'

    inlines = [OtherInline]

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
