from django.urls import path
from .views import IndexView, home, FuncionarioDetalheView, detalhes_funcionario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("home/", home, name='home'),
    path('funcionario-detalhe/<int:id>/', FuncionarioDetalheView.as_view(), name='funcionario-detalhe'),
    path('funcionario/<int:funcionario_id>/', detalhes_funcionario, name='detalhes_funcionario'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)