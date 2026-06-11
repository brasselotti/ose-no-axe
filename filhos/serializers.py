from rest_framework import serializers
from .models import Filho


class FilhoSerializer(serializers.ModelSerializer):
    """Serializer público — usado na listagem geral e pelo próprio filho."""
    class Meta:
        model = Filho
        fields = [
            'id', 'username', 'nome', 'telefone',
            'endereco', 'bairro', 'cidade', 'cep',
            'data_nascimento', 'data_bori', 'filho_iniciado',
            'data_iniciacao', 'ordem_posto', 'orixa',
            'nome_ere', 'madrinha_padrinho', 'mae_pai_pequeno',
            'eh_administrador',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        filho = super().create(validated_data)
        if password:
            filho.set_password(password)
            filho.save()
        return filho


class FilhoDetalheSerializer(FilhoSerializer):
    """Serializer restrito — inclui o Orunkó, acessível apenas por ADM ou pelo próprio filho mediante confirmação."""
    class Meta(FilhoSerializer.Meta):
        fields = FilhoSerializer.Meta.fields + ['orunko']