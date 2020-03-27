from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


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
        raise forms.ValidationError(_('Only the domain "%(domain)s" is allowed'), params={'domain': self.request.domain})

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

