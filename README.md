# URL Home - API de Encurtamento de URLs

Uma API REST para criação e gerenciamento de URLs encurtadas.

Este projeto foi desenvolvido como parte de um desafio técnico backend e demonstra boas práticas de arquitetura, validação de URLs, rastreamento de acessos e testes automatizados.

# Funcionalidades

Criar URLs encurtadas
Redirecionar para a URL original
Consultar detalhes de uma URL
Suporte para alias customizado
Expiração de URLs
Contagem de acessos click tracking
Autenticação básica
Testes automatizados com pytest

# Tecnologias Utilizadas

Python
Django
Django REST Framework
SQLite
pytest
Docker

# 📦 Estrutura do Projeto
url_home/
urls/
controllers/
services/
repositories/
models.py
views.py
tests/
manage.py
requirements.txt
Dockerfile
README.md

O projeto segue uma arquitetura em camadas:
Controller responsável por receber e responder requisições HTTP
Service contém as regras de negócio
Repository responsável pelo acesso ao banco de dados

Essa separação melhora a organização, manutenção e testabilidade do código.

# Endpoints da API

## Criar URL Encurtada
POST /v1/urls
Exemplo de requisição:

{
  "url": "https://example.com",
  "customAlias": "meu-link",
  "expiresAt": "2026-12-31T23:59:59Z"
}

Exemplo de resposta:
{
  "id": "meu-link",
  "shortUrl": "http://localhost:8000/meu-link"
}

## Redirecionar para a URL Original
GET /{shortId}
Exemplo:
GET /abc123

Redireciona automaticamente para a URL original.

## Consultar Detalhes da URL
GET /v1/urls/{id}
Exemplo de resposta:
{
  "id": "abc123",
  "originalUrl": "https://example.com",
  "clickCount": 10,
  "createdAt": "2026-01-01T10:00:00Z"
}

# ▶ Como Executar o Projeto Localmente

## 1 Instalar dependências
pip install -r requirements.txt

## 2 Executar as migrations
python manage.py migrate

## 3 Iniciar o servidor
python manage.py runserver

A API estará disponível em:
http://localhost:8000


# Executando os Testes
Os testes foram implementados utilizando pytest.

Para executar:
pytest

# Executando com Docker
## Construir a imagem
docker build -t url-home-api .

## Executar o container
docker run -p 8000:8000 url-home-api

A aplicação ficará disponível em:
http://localhost:8000

# Autenticação
Alguns endpoints exigem autenticação básica.
Exemplo de header:
Authorization: Basic base64(usuario:senha)

# 📈 Possíveis Melhorias Futuras
Algumas melhorias que poderiam ser adicionadas em um ambiente de produção:

Endpoint para listagem de URLs
Paginação
Cache com Redis
Configuração de deploy para produção

# Autor
Projeto desenvolvido como parte de um desafio técnico para avaliação de habilidades em backend.
