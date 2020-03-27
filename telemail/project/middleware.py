from django.contrib.auth.models import Permission

class DomainMiddleware(object):
    def process_request(self, request):
        if request.user.username.startswith('admin@'):
            request.domain = request.user.username[6:]
        else:
            request.domain = ''
