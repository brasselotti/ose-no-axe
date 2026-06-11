from django.db import models

# Create your models here.
class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada (Doação/Arrecadação)'),
        ('saida', 'Saída (Custo/Despesa)'),
    ]

    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    data = models.DateField()
    observacao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"

    def __str__(self):
        return f"{self.tipo.upper()} - {self.descricao} (R$ {self.valor})"