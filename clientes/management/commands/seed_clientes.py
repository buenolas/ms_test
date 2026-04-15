from django.core.management.base import BaseCommand

from clientes.models import Cliente, TipoCliente

# Lista de clientes iniciais para popular o banco de dados em ambiente de desenvolvimento
# Incluído o campo "ativo" para refletir o status de cada cliente
CLIENTES_INICIAIS = [
    {"nome": "Ana", "email": "ana@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Bruno", "email": "bruno@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Carlos", "email": "carlos@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": False},
    {"nome": "Daniela", "email": "daniela@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": True},
    {"nome": "Eduardo", "email": "eduardo@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": True},
    {"nome": "Fernanda", "email": "fernanda@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": False},
    {"nome": "Gustavo", "email": "gustavo@email.com", "tipo": TipoCliente.PESSOA_JURIDICA, "ativo": True},
    {"nome": "Helena", "email": "helena@email.com", "tipo": TipoCliente.VIP, "ativo": True},
    {"nome": "Igor", "email": "igor@email.com", "tipo": TipoCliente.PESSOA_FISICA, "ativo": False},
    {"nome": "Juliana", "email": "juliana@email.com", "tipo": TipoCliente.VIP, "ativo": True},
]


class Command(BaseCommand):
    help = "Cria clientes iniciais para ambiente de desenvolvimento."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in CLIENTES_INICIAIS:
            cliente, created = Cliente.objects.get_or_create(
                email=item["email"],
                defaults={
                    "nome": item["nome"],
                    "tipo": item["tipo"],
                    "ativo": item["ativo"],
                },
            )

            if created:
                created_count += 1
                continue

            fields_to_update = []
            if cliente.nome != item["nome"]:
                cliente.nome = item["nome"]
                fields_to_update.append("nome")
            if cliente.tipo != item["tipo"]:
                cliente.tipo = item["tipo"]
                fields_to_update.append("tipo")
            if cliente.ativo != item["ativo"]:
                cliente.ativo = item["ativo"]
                fields_to_update.append("ativo")

            if fields_to_update:
                cliente.save(update_fields=fields_to_update)
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed finalizado. Criados: {created_count} | Atualizados: {updated_count}"
            )
        )
