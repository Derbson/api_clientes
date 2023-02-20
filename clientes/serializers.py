from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    # Exibindo todos os Clientes
    class Meta:
        model = Cliente
        fields = '__all__'


