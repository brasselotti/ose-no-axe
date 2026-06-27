from django.contrib import admin
from .models import Mensalidade

# Register your models here.
@admin.register(Mensalidade)
class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ('filho', 'mes_referencia', 'valor', 'status')
    list_filter = ('status', 'mes_referencia')
    search_fields = ('filho__nome',)