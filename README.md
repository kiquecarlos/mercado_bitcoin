# Mercado Bitcoin

Segue abaixo instruções para utilização da aplicação desenvolvida.

Observações: Tempo aplicado ao teste aprox. 7h,
Devido o tempo disponivel para o tete, foi removido a parte de teste, e a configuração do docker, e utilizador Sqlite para Banco de dados.

Atualmente estava a mais de 2 anos sem utilizar python no Back-End

## Tecnologias Utilizadas

Django Restframework

Swagger

Api Logs

Sqlite3

## Estrutura das pastas

```bash
├── backend (Sistema API)
│   ├── migrations
│   └── src (Pastas Principais do Projeto)
│       ├── choices
│       ├── configs (Area para Configurações)
│       ├── controllers(Área de controle)
│       │   └── mms
│       │       └── actions (Area de Ação de cada Requisição)
│       ├── helpers (Codigo Reaproveitavel com regras de n0egocio)
│       │   └── serializers (Conversão dos Dados)
│       ├── middlewares (Ações que serão executadas antes da Action)
│       ├── models(Models do Banco de dados)
│       │   └── base_models
│       ├── routes (Rotas/Urls das Requisições
│       ├── services (Integração com Servicos Externos)
│       │   └── external_apis
│       ├── tests (Área dos Scripts de Teste)
│       └── utils (Pequenas funções para reutilização
│           └── validates
├── core (Aplicação Principal)
├── job (Aplicação Scheduler)
├── scripts (Scripts de Execução)
└── staticfiles (Arquivos Estaticos)
```

## Decisões tomadas

Usar um Job com While True ao invez de um scheduler(Motivo:Tempo)

User um script para start do projeto (Motivo:Facilitar integração/Sincronização)

### Observações sobre o Job:

O Job só enviará e-mail, caso seja inserido os dados na pasta

backend.src.configs.email

## Pré Requesitos

python 3.8

pacote [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

## Instalação

### Step1 (Instalação dos Pacotes):

```bash
pipenv install
```

### Step2 (Entrar na venv):

```bash
pipenv shell
```

### Step3 (Sincronizaçãoe configuração do Projeto):

```bash
pipenv run first_time
```

aqui irá sincronizar os models

executar as migrations

será solicitado cadastro do superuser do Django.

irá sincronizar com API do mercado bitcoin

### Step 4 (Rodando o Projeto):

```bash
pipenv run prod_back
```

```bash
pipenv run prod_job
```

## Documentação API

Documentação Api foi configurado com Swagger
links para documentação

[http://0.0.0.0:8000/doc/swagger/](http://0.0.0.0:8000/doc/swagger/)

[http://0.0.0.0:8000/doc/redoc/](http://0.0.0.0:8000/doc/redoc/)

## Logs

Utilizado o pacote drf-api-logger
