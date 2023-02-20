from rest_framework import viewsets, generics
from .models import Cliente
from .serializers import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    # Exibir Todos os Clientes
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    


