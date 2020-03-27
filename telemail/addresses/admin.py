from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf.urls import patterns
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from telemail.addresses.models import Account, Alias, Other, Forward, ForwardedAddress

def extract_domain(email):
    try:
        return email.split('@', 1)[1]
    except IndexError:
        return ''


class AddressAdminForm(forms.ModelForm):
    def clean_address(self):
        result = self.cleaned_data['address']
        if self.request.user.is_superuser:
            return result
        if self.request.domain == extract_domain(result):
            return result
        raise forms.ValidationError(_('Only domain "%(domain)s" is allowed'), params={'domain': self.request.domain})

class AccountForm(AddressAdminForm):
    class Meta:
        model = Account
        widgets = {
                'password': forms.PasswordInput(render_value=False),
        }


class AddressAdminAdmin(admin.ModelAdmin):
    form = AddressAdminForm

    def get_queryset(self, request):
        qs = super(AddressAdminAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(address__iendswith='@' + request.domain)

    def get_form(self, request, obj=None, **kwargs):
        result = super(AddressAdminAdmin, self).get_form(request, obj, **kwargs)
        result.request = request
        return result

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or not obj:
            return True
        return extract_domain(obj.address) == request.domain

    has_delete_permission = has_change_permission

class AccountAdmin(AddressAdminAdmin):
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

class AliasAdmin(AddressAdminAdmin):
    form = AddressAdminForm
    list_display = ('address', 'others')
    search_fields = ['address', 'aliases__alias']

    def others(self, obj):
        return ', '.join(d.alias for d in obj.aliases.all())
    others.short_description = _('aliases')

    inlines = [OtherInline]

admin.site.register(Alias, AliasAdmin)


class ForwardedAddressInline(admin.TabularInline):
    model = ForwardedAddress
    verbose_name = _('address')
    verbose_name_plural = _('forward to')

class ForwardAdmin(AddressAdminAdmin):
    list_display = ('address', 'forward_to')
    search_fields = ['address', 'destinations__destination']

    def forward_to(self, obj):
        return ', '.join(d.destination for d in obj.destinations.all())
    forward_to.short_description = _('forward to')

    inlines = [ForwardedAddressInline]

admin.site.register(Forward, ForwardAdmin)
