from django.db import models
from filhos.models import Filho  # Vinculando com o app de filhos

# Create your models here.
class Mensalidade(models.Model):
    STATUS_CHOICES = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
        ('atrasado', 'Atrasado'),
        ('recusado', 'Recusado'),
    ]

    # Se o filho for deletado do sistema, as mensalidades dele também somem (CASCADE)
    filho = models.ForeignKey(Filho, on_delete=models.CASCADE, related_name='mensalidades')
    mes_referencia = models.DateField(help_text="Use o dia 1 do mês correspondente")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pendente')
    comprovante = models.FileField(upload_to='comprovantes/', null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Mensalidade"
        verbose_name_plural = "Mensalidades"

    def __str__(self):
        return f"Mensalidade de {self.filho.nome} - {self.mes_referencia.strftime('%m/%Y')}"

class IsentoMes(models.Model):
    filho = models.ForeignKey(Filho, on_delete=models.CASCADE, related_name='isencoes')
    mes_referencia = models.DateField(help_text="Use o dia 1 do mês correspondente")
    motivo = models.TextField(blank=True)
    criado_por = models.ForeignKey(
        Filho,
        on_delete=models.SET_NULL,
        null=True,
        related_name='isencoes_criadas'
    )

    class Meta:
        verbose_name = "Isenção de Mês"
        verbose_name_plural = "Isenções de Mês"
        unique_together = ('filho', 'mes_referencia')

    def __str__(self):
        return f'{self.filho.nome} - {self.mes_referencia.strftime("%m/%Y")}'