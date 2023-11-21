from django.shortcuts import render
from .models import Funcionario
from django.views.generic import TemplateView
from django.views.generic import ListView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        return context

def home(request):
    query = request.GET.get('q')
    funcionarios = Funcionario.objects.all()

    if query:
        funcionarios = funcionarios.filter(nome__icontains=query)

    return render(request, 'index.html', {'funcionarios': funcionarios})

class FuncionarioDetalheView(ListView):
    template_name = 'funcionario-detail.html'
    paginate_by = 5
    ordering = 'nome'
    model = Funcionario

    def get_context_data(self, **kwargs):
        context = super(FuncionarioDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['funcionario'] = Funcionario.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Funcionario.objects.filter(funcionario_id=id)