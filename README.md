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
- Adição e uso do campo `ativo` no model `Cliente`.
- Criação de API REST com Django REST Framework para o recurso de clientes.
- Implementação de listagem com regra de negócio:
- `GET /api/clientes/` retorna apenas clientes ativos por padrão.
- `GET /api/clientes/?todos=1` retorna ativos e inativos.
- Implementação de inativação/reativação via:
- `PATCH /api/clientes/<id>/` com payload `{ "ativo": true/false }`.
- Organização do projeto com settings por ambiente:
- `ms_test/settings/base.py`
- `ms_test/settings/dev.py`
- Padronização da camada DRF com paginação, renderers/parsers e tratamento padrão de exceções.
- Reorganização dos testes em módulos:
- `clientes/tests/test_api_clientes.py`
- `clientes/tests/test_seed_clientes.py`
- Atualização do comando `seed_clientes` para manter idempotência e preencher corretamente o campo `ativo`.

No frontend (Angular):
- Criação de um novo projeto frontend separado em `frontend/`.
- Implementação de consumo dos endpoints do backend:
- listagem de clientes
- filtro para incluir inativos
- ação de inativar/reativar por botão
- Criação de service para centralizar chamadas HTTP (`clientes-api.service.ts`).
- Uso de proxy local (`proxy.conf.json`) para facilitar integração backend/frontend durante desenvolvimento.

### 6.2. Decisões técnicas tomadas

- Foi escolhida a abordagem RESTful com `PATCH` no próprio recurso `Cliente`, em vez de criar endpoints separados como `/inativar/` e `/reativar/`.
- O backend foi finalizado antes do frontend para garantir que o Angular consumisse uma API estável e testada.
- A regra de filtro foi mantida no backend (e não no frontend), preservando a regra de negócio centralizada.
- A estrutura de testes foi separada por domínio para aumentar legibilidade e manutenção.
- O frontend foi mantido simples e funcional, alinhado ao objetivo do teste (clareza e organização acima de complexidade).

### 6.3. Observações importantes e desafios

Durante a implementação, o principal desafio foi a transição da estrutura inicial baseada em views/templates Django para uma arquitetura orientada a API com DRF.

Como eu ainda não tinha experiência prática com Django REST Framework, tive dificuldade inicial para entender:
- a estrutura ideal de arquivos (serializer, viewset, router, urls);
- como adaptar a regra de listagem e atualização para os endpoints DRF;
- como reorganizar o projeto sem perder clareza.

Para superar esse ponto, conduzi pesquisas em documentação oficial e utilizei IA como apoio para acelerar a produtividade, sempre validando tecnicamente as decisões e o comportamento final do código.

O uso de IA foi um apoio de produtividade e organização, sem substituir entendimento: toda alteração foi testada e revisada para garantir domínio sobre a implementação.

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

Observação:
- O frontend está configurado para consumir o backend via proxy local.
- Para funcionar corretamente, rode backend e frontend ao mesmo tempo em terminais separados.

### 6.5. Como rodar os testes

Backend:

```bash
python manage.py test
```
