from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return super(HomePageView, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['section'] = "home"
        return context
