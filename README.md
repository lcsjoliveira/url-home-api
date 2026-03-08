# URL Shortener API

API para encurtamento de URLs desenvolvida com Django.

O projeto permite:

- Criar URLs encurtadas
- Redirecionar para a URL original
- Consultar informações da URL
- Contabilizar número de cliques
- Definir expiração
- Utilizar alias customizado

# Tecnologias utilizadas

- Python 3.12
- Django 6
- Pytest
- Docker

# Arquitetura

O projeto foi organizado em camadas para manter separação de responsabilidades.
url_home/
views.py → camada HTTP
services.py → regras de negócio
repository.py → acesso ao banco de dados
validators.py → validações
utils.py → utilidades
auth.py → autenticação via API Key

# Instalação do projeto
Clone o repositório:
git clone https://github.com/lcsjoliveira/url-home-api.git
cd url-home-api

Crie o ambiente virtual:
python -m venv venv

Ative o ambiente:
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Execute as migrations:
python manage.py migrate

Inicie o servidor:
python manage.py runserver

# Autenticação
A API utiliza autenticação simples por API Key.

Header necessário:
X-API-KEY: test-api-key

# Endpoints da API
## Criar URL encurtada
POST
/v1/urls

Body:
{
"originalUrl": "https://google.com"
}

Exemplo usando curl:
curl -X POST http://localhost:8000/v1/urls
-H "Content-Type: application/json"
-H "X-API-KEY: test-api-key"
-d '{
"originalUrl": "https://google.com"
}'

Resposta esperada:
{
"id": "abc123",
"shortUrl": "http://localhost:8000/abc123",
"originalUrl": "https://google.com"
}

## Redirecionar URL
GET
/{id}

Exemplo:
http://localhost:8000/abc123

## Consultar detalhes da URL
GET
/v1/urls/{id}

Resposta:
{
"id": "abc123",
"shortUrl": "http://localhost:8000/abc123",
"originalUrl": "https://google.com",
"createdAt": "...",
"expirationDate": null,
"clickCount": 5
}

# Rodando os testes
Execute:
pytest

O projeto possui:
- testes unitários
- testes de integração

# Executando com Docker
Build da imagem:
docker build -t url-shortener .

Rodar container:
docker run -p 8000:8000 url-shortener

# Decisões técnicas
Algumas decisões adotadas no projeto:
- Uso de Django para acelerar o desenvolvimento da API
- Separação em camadas service, repository para melhorar manutenção
- Pytest para facilitar testes automatizados
- API Key simples para autenticação da API
- Docker para facilitar execução em qualquer ambiente

# Autor
Lucas Oliveira