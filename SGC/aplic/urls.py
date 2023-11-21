from django.urls import path
from .views import IndexView, home, FuncionarioDetalheView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("", home, name='home'),
    path('funcionario-detalhe/<int:id>/', FuncionarioDetalheView.as_view(), name='funcionario-detalhe'),
]
