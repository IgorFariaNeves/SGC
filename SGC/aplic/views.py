from django.views.generic import TemplateView
from aplic.models import Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        return context

