from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from clientes.models import Cliente, TipoCliente

# Testes para a API de clientes, cobrindo listagem, atualização e métodos não permitidos
class ClienteAPITests(APITestCase):
    # Configura o ambiente de teste criando clientes ativos e inativos para validar os diferentes cenários de listagem e atualização
    def setUp(self):
        self.cliente_1 = Cliente.objects.create(
            nome="Ana",
            email="ana@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
            ativo=True,
        )
        self.cliente_2 = Cliente.objects.create(
            nome="Bruno",
            email="bruno@email.com",
            tipo=TipoCliente.PESSOA_JURIDICA,
            ativo=False,
        )

    # Testa que a listagem padrão retorna apenas clientes ativos
    def test_listagem_padrao_retorna_apenas_ativos(self):
        response = self.client.get(reverse("cliente-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["id"], self.cliente_1.id)
        self.assertTrue(response.data["results"][0]["ativo"])

    # Testa que a listagem com ?todos=1 retorna ativos e inativos
    def test_listagem_com_todos_retorna_ativos_e_inativos(self):
        response = self.client.get(f'{reverse("cliente-list")}?todos=1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        returned_ids = {item["id"] for item in response.data["results"]}
        self.assertEqual(returned_ids, {self.cliente_1.id, self.cliente_2.id})

    # Testa que o PATCH para inativar um cliente funciona
    def test_patch_ativo_false_inativa_cliente(self):
        response = self.client.patch(
            reverse("cliente-detail", args=[self.cliente_1.id]),
            {"ativo": False},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente_1.refresh_from_db()
        self.assertFalse(self.cliente_1.ativo)

    # Testa que o PATCH para reativar um cliente inativo funciona mesmo sem ?todos=1
    def test_patch_cliente_inativo_sem_todos_funciona(self):
        response = self.client.patch(
            reverse("cliente-detail", args=[self.cliente_2.id]),
            {"ativo": True},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente_2.refresh_from_db()
        self.assertTrue(self.cliente_2.ativo)

    # Testa métodos não permitidos retornam 405
    def test_metodos_nao_permitidos_retorna_405(self):
        post_response = self.client.post(
            reverse("cliente-list"),
            {"nome": "Novo", "email": "novo@email.com", "tipo": "PF"},
            format="json",
        )
        delete_response = self.client.delete(
            reverse("cliente-detail", args=[self.cliente_1.id])
        )

        self.assertEqual(post_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(delete_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
