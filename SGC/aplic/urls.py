from django.urls import path
from .views import IndexView, home, FuncionarioDetalheView, detalhes_funcionario

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("home/", home, name='home'),
    path('funcionario-detalhe/<int:id>/', FuncionarioDetalheView.as_view(), name='funcionario-detalhe'),
    path('funcionario/<int:funcionario_id>/', detalhes_funcionario, name='detalhes_funcionario'),
]
