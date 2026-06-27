import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Mensalidade
from financeiro.models import Movimentacao


@receiver(post_save, sender=Mensalidade)
def criar_movimentacao_ao_aprovar(sender, instance, created, **kwargs):
    """Quando uma mensalidade é aprovada, cria automaticamente uma movimentação de entrada."""
    if instance.status != 'pago':
        return

    ja_existe = Movimentacao.objects.filter(
        descricao=f'Mensalidade - {instance.filho.nome} ({instance.mes_referencia.strftime("%m/%Y")})',
        data=instance.data_pagamento,
        valor=instance.valor,
        tipo='entrada',
    ).exists()

    if not ja_existe:
        Movimentacao.objects.create(
            descricao=f'Mensalidade - {instance.filho.nome} ({instance.mes_referencia.strftime("%m/%Y")})',
            valor=instance.valor,
            tipo='entrada',
            data=instance.data_pagamento,
            observacao=f'Referente a {instance.mes_referencia.strftime("%m/%Y")}',
        )


@receiver(post_delete, sender=Mensalidade)
def remover_movimentacao_ao_excluir(sender, instance, **kwargs):
    """Quando uma mensalidade aprovada é excluída, remove a movimentação correspondente."""
    if instance.status == 'pago':
        Movimentacao.objects.filter(
            descricao=f'Mensalidade - {instance.filho.nome} ({instance.mes_referencia.strftime("%m/%Y")})',
            data=instance.data_pagamento,
            valor=instance.valor,
            tipo='entrada',
        ).delete()

    if instance.comprovante:
        if os.path.isfile(instance.comprovante.path):
            os.remove(instance.comprovante.path)