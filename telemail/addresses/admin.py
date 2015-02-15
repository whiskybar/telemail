from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf.urls import patterns
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
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

    def get_urls(self):
        urls = super(AccountAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^batch/$', self.admin_site.admin_view(self.batch)),
        )
        return my_urls + urls

    def batch(self, request):
        if request.method == 'POST':
            return HttpResponseRedirect('/thanks/')
        else:
            form = None
        app_label = Account._meta.app_label
        return render(request, 'admin/addresses/account/batch.html', {
            'app_label': app_label,
            'form': form,
        })

admin.site.register(Account, AccountAdmin)


class OtherInline(admin.TabularInline):
    model = Other
    verbose_name = _('alias')
    verbose_name_plural = _('aliases')

class AliasAdmin(admin.ModelAdmin):
    list_display = ('address', 'others')
    search_fields = ['address', 'aliases_alias']

    def others(self, obj):
        return ', '.join(d.alias for d in obj.aliases.all())
    others.short_description = _('aliases')

    inlines = [OtherInline]

admin.site.register(Alias, AliasAdmin)


class ForwardedAddressInline(admin.TabularInline):
    model = ForwardedAddress
    verbose_name = _('address')
    verbose_name_plural = _('forward to')

class ForwardAdmin(admin.ModelAdmin):
    list_display = ('address', 'forward_to')
    search_fields = ['address', 'destinations__destination']
   
    def forward_to(self, obj):
        return ', '.join(d.destination for d in obj.destinations.all())
    forward_to.short_description = _('forward to')
    
    inlines = [ForwardedAddressInline]

admin.site.register(Forward, ForwardAdmin)
