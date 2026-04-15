from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet

# Define as rotas para a API de clientes usando um router do Django REST Framework, registrando o viewset de clientes com o prefixo "clientes" e o basename "cliente"
router = DefaultRouter()
router.register("clientes", ClienteViewSet, basename="cliente")

urlpatterns = router.urls
