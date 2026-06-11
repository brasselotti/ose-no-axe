from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from filhos.views import FilhoViewSet, filhos_lista, filho_cadastrar, filho_editar, filho_excluir
from financeiro.views import MovimentacaoViewSet, financeiro_lista, movimentacao_registrar, movimentacao_excluir
from mensalidades.views import MensalidadeViewSet, mensalidades_lista, mensalidade_registrar, mensalidade_aprovar, mensalidade_negar, mensalidade_excluir, isentar_filho
from osenoaxe.views import login_view, logout_view, home_view, perfil_view



router = DefaultRouter()
router.register(r'filhos', FilhoViewSet, basename='filhos')
router.register(r'movimentacoes', MovimentacaoViewSet, basename='movimentacoes')
router.register(r'mensalidades', MensalidadeViewSet, basename='mensalidades')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Views HTML
    path('', redirect_to_login := lambda req: __import__('django.shortcuts', fromlist=['redirect']).redirect('/login/')),
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
    path('mensalidades/isentar/<int:filho_id>/', isentar_filho, name='isentar_filho'),


    # Rotas de Financeiro
    path('financeiro/', financeiro_lista, name='financeiro_lista'),
    path('financeiro/registrar/', movimentacao_registrar, name='movimentacao_registrar'),
    path('financeiro/<int:pk>/excluir/', movimentacao_excluir, name='movimentacao_excluir'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)