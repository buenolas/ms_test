# Teste Prático — Desenvolvedor(a) Júnior Python/Django

## 1. Objetivo do teste

Este teste tem como objetivo avaliar sua capacidade de realizar uma pequena evolução em um projeto Django já existente, de forma funcional, organizada e coerente.

No dia a dia do MB, grande parte do trabalho envolve:
- entender requisitos simples de negócio
- alterar código existente
- ajustar models, views, templates e queries
- implementar mudanças com cuidado
- validar o comportamento da funcionalidade
- explicar com clareza o que foi feito

Este teste foi pensado para simular esse tipo de cenário de forma objetiva e justa.

---

## 2. Contexto

Você recebeu um projeto Django base já funcional com um módulo de clientes.

Atualmente:
- existe um model `Cliente`
- existe uma listagem de clientes
- os clientes cadastrados aparecem normalmente na tela

Precisamos evoluir esse projeto para permitir a **inativação e reativação de clientes**, além de ajustar a listagem para respeitar essa regra.

---

## 3. Desafio

Implementar a funcionalidade de **inativação de clientes**, fazendo com que clientes inativos não apareçam na listagem padrão.

---

## 4. Requisitos obrigatórios

### 4.1. Alteração no model
1. Adicionar ao model `Cliente` o campo `ativo`
2. Exibir apenas clientes ativos por padrão
3. Permitir visualizar todos os clientes com filtro opcional
4. Criar forma de inativar e reativar clientes
5. Criar pelo menos 2 testes automatizados
6. Atualizar o `seed_clientes` para gerar uma massa de dados
7. Separe o backend do frontend, para boas práticas de desenvolvimento:
- O frontend será feito em um novo projeto que irá acessar as informações deste projeto;
- O frontend deve ser feito em Angular e consumir endpoints do backend;
- Pode utilizar no backend o DRF (Django Rest Framework) para criação dos endpoints;
8. A melhor solução para este teste não é a mais complexa e sim:
- a mais simples;
- a mais clara;
- a mais funcional;
- a mais organizada;
9. Ao final, atualize este README com uma seção chamada "O que foi implementado", descrevendo brevemente:
- o que você fez;
- eventuais decisões tomadas;
- qualquer observação importante sobre sua implementação;
- como rodar o projeto completo, dividido em backend e frontend.
10. Você pode utilizar IA como apoio no desenvolvimento, porém esperamos que você:
- entenda o que implementou
- consiga explicar suas escolhas
- consiga responder perguntas simples sobre o próprio código
11. Junto com a entrega faça um vídeo de no máximo 10 minutos explicando o que foi feito, junto com as envidências do software rodando.

---

## 5. Bônus inicial:

```python
## Como rodar o projeto
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

## 6. O que foi implementado

### 6.1. O que foi feito

No backend (Django + DRF):
- Adição do campo `ativo` no model `Cliente`.
- Criação de endpoints com Django REST Framework para listagem e atualização de clientes.
- Implementação da regra de negócio para exibir apenas clientes ativos por padrão.
- Implementação de filtro opcional para listar também os clientes inativos com `GET /api/clientes/?todos=1`.
- Implementação de inativação e reativação via `PATCH /api/clientes/<id>/`, atualizando apenas o campo `ativo`.
- Atualização do comando `seed_clientes` para gerar uma massa de dados com clientes ativos e inativos, mantendo comportamento idempotente.
- Reforço dos testes automatizados para cobrir os principais cenários da API e do seed.
- Organização do projeto com separação de settings em:
- `ms_test/settings/base.py`
- `ms_test/settings/dev.py`

No frontend (Angular):
- Criação de um projeto frontend separado em `frontend/`.
- Consumo dos endpoints do backend para:
- listagem de clientes
- filtro para exibir todos os clientes
- ação de inativar e reativar por botão
- Criação de um service para centralizar a comunicação HTTP com a API (`clientes-api.service.ts`).
- Uso de proxy local (`proxy.conf.json`) para facilitar a integração entre frontend e backend durante o desenvolvimento.

### 6.2. Decisões técnicas tomadas

- Foi escolhida a abordagem REST com `PATCH` no próprio recurso `Cliente`, em vez de criar endpoints separados para inativar e reativar.
- A regra de filtro foi mantida no backend, centralizando a regra de negócio no lugar certo.
- A listagem da API foi mantida sem paginação, para simplificar o consumo no frontend e evitar complexidade desnecessária para o escopo deste teste.
- O frontend foi mantido simples e direto, priorizando clareza, organização e funcionamento.
- Os testes foram organizados por responsabilidade, separando cenários da API e do comando de seed.

### 6.3. Observações importantes

- O projeto foi ajustado de uma estrutura mais próxima de views/templates para uma arquitetura baseada em API no backend e Angular no frontend.
- Durante a implementação, busquei manter a solução o mais simples possível, evitando camadas ou recursos desnecessários para o escopo do teste.
- Também revisei a entrega para remover pontos que poderiam gerar inconsistência, como paginação sem uso no frontend e código legado que não fazia mais parte do fluxo principal.
- Utilizei documentação oficial e IA como apoio pontual de pesquisa e organização, sempre validando o comportamento final do código e das decisões adotadas.

### 6.4. Como rodar o projeto completo (backend e frontend)

Pré-requisitos:
- Python 3.x
- Node.js + npm

Backend (Django):

```bash
python -m venv .venv
.venv\Scripts\activate
copy .env.example .env
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_clientes
python manage.py runserver
```

Backend em: `http://127.0.0.1:8000`

Endpoints principais:
- `GET /api/clientes/`
- `GET /api/clientes/?todos=1`
- `PATCH /api/clientes/<id>/`

Frontend (Angular):

```bash
cd frontend
npm install
npm start
```

Frontend em: `http://localhost:4200`

Observações:
- O frontend está configurado para consumir o backend via proxy local.
- Para o funcionamento completo da aplicação, backend e frontend devem ser executados ao mesmo tempo em terminais separados.

### 6.5. Como rodar os testes

```bash
python manage.py test
```

