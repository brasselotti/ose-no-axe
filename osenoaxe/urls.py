from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from filhos.views import filhos_lista, filho_cadastrar, filho_editar, filho_excluir
from financeiro.views import financeiro_lista, movimentacao_registrar, movimentacao_excluir
from mensalidades.views import mensalidades_lista, mensalidade_registrar, mensalidade_aprovar, mensalidade_negar, mensalidade_excluir, isentar_filho, isentar_remover
from osenoaxe.views import login_view, logout_view, home_view, perfil_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Views HTML
    path('', RedirectView.as_view(url='/login/')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('perfil/', perfil_view, name='perfil'),

    # Rotas de Filhos
    path('filhos/', filhos_lista, name='filhos_lista'),
    path('filhos/cadastrar/', filho_cadastrar, name='filho_cadastrar'),
    path('filhos/<int:pk>/editar/', filho_editar, name='filho_editar'),
    path('filhos/<int:pk>/excluir/', filho_excluir, name='filho_excluir'),

    # Rotas de Mensalidades
    path('mensalidades/', mensalidades_lista, name='mensalidades_lista'),
    path('mensalidades/registrar/', mensalidade_registrar, name='mensalidade_registrar'),
    path('mensalidades/<int:pk>/aprovar/', mensalidade_aprovar, name='mensalidade_aprovar'),
    path('mensalidades/<int:pk>/negar/', mensalidade_negar, name='mensalidade_negar'),
    path('mensalidades/<int:pk>/excluir/', mensalidade_excluir, name='mensalidade_excluir'),
    path('mensalidades/isentar/<int:pk>/', isentar_filho, name='isentar_filho'),
    path('mensalidades/isentar/<int:isento_id>/remover/', isentar_remover, name='isentar_remover'),


    # Rotas de Financeiro
    path('financeiro/', financeiro_lista, name='financeiro_lista'),
    path('financeiro/registrar/', movimentacao_registrar, name='movimentacao_registrar'),
    path('financeiro/<int:pk>/excluir/', movimentacao_excluir, name='movimentacao_excluir'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)