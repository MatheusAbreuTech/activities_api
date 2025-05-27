Claro! Aqui está um exemplo de `README.md` explicando como rodar o projeto com Docker, incluindo o passo da criação da rede compartilhada `api-network`.

---

````markdown
# Projeto Multi-API com Docker

Este projeto é composto por múltiplas APIs (como `api_semester_project` e `activities_api`) que se comunicam entre si por meio de containers Docker.

## 📦 Estrutura

- `web/`
  - Contém o serviço `api-gerenciamento-escolar` e o banco de dados MySQL.
- `atividade_service/`
  - Contém o serviço `atividade_service`.
- `pessoa_service/`
  - Contém o serviço `pessoa_service`.

As APIs se comunicam utilizando uma rede Docker compartilhada chamada `api-network`.

---

## 🚀 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🌐 Criando a rede compartilhada

Antes de subir os serviços, você precisa criar manualmente a rede Docker externa `api-network`:

```bash
docker network create api-network
````

> Esse passo precisa ser feito **apenas uma vez**, a menos que você remova a rede posteriormente.

---

## 🔧 Como rodar os serviços

### 1. Clone os repositórios

```bash
git clone https://github.com/MatheusAbreuTech/activities_api.git
git clone https://github.com/MatheusAbreuTech/api_semester_project.git
```

### 2. Suba o `api_semester_project-1`

No diretório `api_semester_project-1`:

```bash
docker compose up --build
```

> Isso irá iniciar o serviço `web` na porta `5000` e o banco de dados MySQL.

---

### 3. Suba o `activities_api-2` (pessoa\_service + atividade\_service)

Em outro terminal, no diretório `activities_api`:

```bash
docker compose up --build
```

> Isso irá iniciar os serviços `pessoa_service` na porta `5001` e `atividade_service` na porta `5002`.

---

## 🔗 Comunicação entre APIs

Os serviços se comunicam por meio do nome dos containers. Por exemplo:

* O `pessoa_service` se comunica com o `web` através da URL:

  ```
  http://web:5000/alunos/1
  ```

---

## 🧹 Parar os containers

Para parar os serviços:

```bash
docker compose down
```

Faça isso em ambos os diretórios (`api_semester_project` e `activities_api`) se necessário.

---

## 📌 Observações

* Certifique-se de que a rede `api-network` existe antes de subir os serviços.
* A comunicação entre serviços só funciona porque todos estão conectados à **mesma rede externa**.

