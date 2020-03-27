from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from telemail.domains.models import DomainTrash


class DomainTrashForm(forms.ModelForm):
    def clean_domain(self):
        result = self.cleaned_data['domain']
        if self.request.user.is_superuser:
            return result
        if self.request.domain == result:
            return result
        raise forms.ValidationError(_('Only the domain "%(domain)s" is allowed'), params={'domain': self.request.domain})


class DomainTrashAdmin(admin.ModelAdmin):
    form = DomainTrashForm

    list_display = ('domain', 'trash')
    search_fields = ['domain', 'trash']

    def get_queryset(self, request):
        qs = super(DomainTrashAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(domain=request.domain)

    def get_form(self, request, obj=None, **kwargs):
        result = super(DomainTrashAdmin, self).get_form(request, obj, **kwargs)
        result.request = request
        return result

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or not obj:
            return True
        return obj.domain == request.domain

    has_delete_permission = has_change_permission

admin.site.register(DomainTrash, DomainTrashAdmin)

#admin.site.unregister(Group)
