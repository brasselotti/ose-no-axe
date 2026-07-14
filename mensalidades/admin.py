from django.contrib import admin
from .models import Mensalidade, IsentoMes

@admin.register(Mensalidade)
class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ('filho', 'mes_referencia', 'valor', 'status')
    list_filter = ('status', 'mes_referencia')
    search_fields = ('filho__nome',)

@admin.register(IsentoMes)
class IsentoMesAdmin(admin.ModelAdmin):
    list_display = ('filho', 'mes_referencia', 'criado_por', 'motivo')
    list_filter = ('mes_referencia',)
    search_fields = ('filho__nome',)