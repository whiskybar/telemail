class DomainMiddleware(object):
    def process_request(self, request):
        try:
            user, domain = request.user.username.split('@', 1)
        except ValueError:
            request.domain = ''
        else:
            if user == 'admin':
                request.domain = domain
            else:
                request.domain = ''
