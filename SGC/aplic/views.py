from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario
from .forms import FuncionarioSearchForm
from typing import Any

class IndexView(ListView):
    template_name = 'index.html'
    model = Funcionario
    context_object_name = 'funcionarios'
    paginate_by = 5
    ordering = 'nome'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = FuncionarioSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Funcionario.objects.all()
        nome = self.request.GET.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

def home(request):
    form = FuncionarioSearchForm(request.GET)
    funcionarios = Funcionario.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        if nome:
            funcionarios = funcionarios.filter(nome__icontains=nome)

    return render(request, 'index.html', {'funcionarios': funcionarios, 'form': form})

class FuncionarioDetalheView(ListView):
    template_name = 'funcionario-detalhe.html'
    model = Funcionario
    context_object_name = 'funcionario'
    paginate_by = 5
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['funcionario'] = Funcionario.objects.get(id=id)
        return context

def detalhes_funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    return render(request, 'funcionario-detalhe.html', {'funcionario': funcionario})
