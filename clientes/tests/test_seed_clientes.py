from django.core.management import call_command
from django.test import TestCase

from clientes.models import Cliente


class SeedClientesCommandTests(TestCase):
    def test_seed_cria_ao_menos_10_clientes_e_eh_idempotente(self):
        call_command("seed_clientes")
        total_apos_primeira_execucao = Cliente.objects.count()

        self.assertGreaterEqual(total_apos_primeira_execucao, 10)

        call_command("seed_clientes")
        self.assertEqual(Cliente.objects.count(), total_apos_primeira_execucao)

    def test_seed_cria_clientes_ativos_e_inativos(self):
        call_command("seed_clientes")

        self.assertTrue(Cliente.objects.filter(ativo=True).exists())
        self.assertTrue(Cliente.objects.filter(ativo=False).exists())
