from django.urls import path, include, re_path
from .views import home, \
    lista_pessoas, \
    lista_veiculos, \
    lista_mensalistas, \
    lista_movmensalistas, \
    lista_movrotativos, \
    pessoa_novo, \
    veiculo_novo, \
    mensalista_novo, \
    movmensalista_novo, \
    movrotativo_novo, \
    pessoa_update, \
    veiculo_update, \
    mensalista_update, \
    movmensalista_update, \
    movrotativo_update, \
    pessoa_delete, \
    veiculo_delete, \
    mensalista_delete, \
    movmensalista_delete, \
    movrotativo_delete

urlpatterns = [
    path('', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa_novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa_update/(?P<id>\d+)$',
            pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoa_delete/(?P<id>\d+)$',
            pessoa_delete, name='core_pessoa_delete'),
    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo_novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo_update/(?P<id>\d+)$',
            veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculo_delete/(?P<id>\d+)$',
            veiculo_delete, name='core_veiculo_delete'),
    re_path(r'^mensalistas/$', lista_mensalistas,
            name='core_lista_mensalistas'),
    re_path(r'^mensalista_novo/$', mensalista_novo,
            name='core_mensalista_novo'),
    re_path(r'^mensalista_update/(?P<id>\d+)$', mensalista_update,
            name='core_mensalista_update'),
    re_path(r'^mensalista_delete/(?P<id>\d+)$',
            mensalista_delete, name='core_mensalista_delete'),
    re_path(r'^movmensalistas/$', lista_movmensalistas,
            name='core_lista_movmensalistas'),
    re_path(r'^movmensalista_novo/$', movmensalista_novo,
            name='core_movmensalista_novo'),
    re_path(r'^movmensalista_update/(?P<id>\d+)$', movmensalista_update,
            name='core_movmensalista_update'),
    re_path(r'^movmensalista_delete/(?P<id>\d+)$',
            movmensalista_delete, name='core_movmensalista_delete'),
    re_path(r'^movrotativos/$', lista_movrotativos,
            name='core_lista_movrotativos'),
    re_path(r'^movrotativo_novo/$', movrotativo_novo,
            name='core_movrotativo_novo'),
    re_path(r'^movrotativo_update/(?P<id>\d+)$', movrotativo_update,
            name='core_movrotativo_update'),
    re_path(r'^movrotativo_delete/(?P<id>\d+)$',
            movrotativo_delete, name='core_movrotativo_delete'),
]
