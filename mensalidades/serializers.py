from rest_framework import serializers
from .models import Mensalidade


class MensalidadeSerializer(serializers.ModelSerializer):
    filho_nome = serializers.CharField(source='filho.nome', read_only=True)

    class Meta:
        model = Mensalidade
        fields = [
            'id', 'filho', 'filho_nome', 'mes_referencia',
            'valor', 'status', 'comprovante', 'data_pagamento',
        ]