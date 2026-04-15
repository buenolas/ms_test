from django.core.management import call_command
from django.test import TestCase

from clientes.models import Cliente

# Testes para o comando de gerenciamento "seed_clientes", garantindo que ele cria clientes iniciais e é idempotente
class SeedClientesCommandTests(TestCase):
    def test_seed_cria_ao_menos_10_clientes_e_eh_idempotente(self):
        call_command("seed_clientes")
        self.assertGreaterEqual(Cliente.objects.count(), 10)

        call_command("seed_clientes")
        self.assertEqual(Cliente.objects.count(), 10)
