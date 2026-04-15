from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer
from .services import get_clientes_queryset

# Define o viewset para a API de clientes, utilizando o serializer e queryset apropriados, e limitando os métodos HTTP permitidos a GET e PATCH
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    http_method_names = ["get", "patch", "head", "options"]

    # Sobrescreve o método get_queryset para aplicar a lógica de negócios definida em get_clientes_queryset, permitindo controlar a inclusão de clientes inativos e o acesso durante atualizações parciais
    def get_queryset(self):
        return get_clientes_queryset(
            include_inactive=self.request.query_params.get("todos") == "1",
            for_partial_update=self.action == "partial_update",
        )
