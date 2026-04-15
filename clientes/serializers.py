from rest_framework import serializers
from .models import Cliente

# Serializer para o modelo Cliente, definindo os campos que serão expostos na API
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "email", "tipo", "ativo", "criado_em"]