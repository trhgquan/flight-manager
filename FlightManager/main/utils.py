from django.views import View

class PaginatedFilterView(View):
    '''A custom Filter View supports Pagination,
    which just parse the querystring back to context.

    This querystring will be parsed to paginator for later results.
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET:
            querystring = self.request.GET.copy()
            if self.request.GET.get('page'):
                del querystring['page']
            
            context['querystring'] = querystring.urlencode()
        
        return context