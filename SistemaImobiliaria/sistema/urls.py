from django.urls import path
from sistema.views import homeSistema, cadastro, incluirCliente, incluirUsuario, incluirImovel

urlpatterns = [
    path('', homeSistema, name='home-sistema'),
    path('cadastro/',cadastro, name='cadastro'),
    path('cadastro/incluir-clientes/',incluirCliente, name='cadastro-cliente'),
    path('cadastro/incluir-usuario/',incluirUsuario, name='cadastro-usuario'),
    path('cadastro/incluir-imovel/',incluirImovel, name='cadastro-imovel')
]