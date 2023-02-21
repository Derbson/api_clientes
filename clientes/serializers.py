from rest_framework import serializers
from .models import Cliente
from .validators import *

class ClienteSerializer(serializers.ModelSerializer):
    # Exibindo todos os Clientes
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"O CPF deve ter 11 dígitos."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"Não inclua números neste campo."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular":"Celular deve ter 11 dígitos."})
        return data
        

        