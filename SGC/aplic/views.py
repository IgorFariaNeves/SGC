from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario

class IndexView(ListView):
    template_name = 'index.html'
    model = Funcionario
    context_object_name = 'funcionarios'
    paginate_by = 5
    ordering = 'nome'

def home(request):
    query = request.GET.get('q')
    funcionarios = Funcionario.objects.all()

    if query:
        funcionarios = funcionarios.filter(nome__icontains=query)

    return render(request, 'index.html', {'funcionarios': funcionarios})

class FuncionarioDetalheView(ListView):
    template_name = 'funcionario-detalhe.html'
    model = Funcionario
    context_object_name = 'funcionario'
    paginate_by = 5
    ordering = 'nome'

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Funcionario.objects.filter(id=id)


def detalhes_funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    return render(request, 'funcionario-detalhe.html', {'funcionario': funcionario})
