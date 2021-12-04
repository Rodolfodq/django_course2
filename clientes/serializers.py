from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, celuar_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "CPF inválido"}
            )
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"}
            )
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': "RG deve conter 9 caracteres"}
            )
        if not celuar_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': "Celular não é valido"}
            )
        return data

