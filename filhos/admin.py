from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filho


@admin.register(Filho)
class FilhoAdmin(UserAdmin):
    fieldsets = (
        ('Identificação Básica', {
            'fields': ('username', 'password', 'nome', 'data_nascimento', 'data_bori', 'eh_administrador')
        }),
        ('Contato e Endereço', {
            'fields': ('telefone', 'endereco', 'bairro', 'cidade', 'cep')
        }),
        ('Status Litúrgico', {
            'fields': ('filho_iniciado',)
        }),
        ('Dados da Iniciação / Feitura', {
            'fields': ('data_iniciacao', 'ordem_posto', 'orixa', 'orunko', 'nome_ere', 'madrinha_padrinho', 'mae_pai_pequeno')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        ('Criar Filho', {
            'fields': ('username', 'password1', 'password2', 'nome', 'eh_administrador')
        }),
    )

    list_display = ('nome', 'username', 'telefone', 'filho_iniciado', 'eh_administrador')
    search_fields = ('nome', 'username', 'orunko')
    list_filter = ('filho_iniciado', 'eh_administrador', 'orixa')


admin.site.site_title = "Osé no Axé"
admin.site.site_header = "Osé no Axé"
admin.site.index_title = "Painel Administrativo - Ilê Axé Afinká"