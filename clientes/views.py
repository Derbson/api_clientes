from rest_framework import viewsets, filters
from .models import Cliente
from .serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    # Exibir Todos os Clientes
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['nome']
    ordering_fields = ['id','nome']
    filterset_fields = ['ativo']

    


