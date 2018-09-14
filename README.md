# Consumo de REST API com Django Rest Framework

Projeto com exemplo simples de como consumir uma REST API usando django rest framework.

## Para emular um servidor JSON, estamos utilizando o projeto [json-server](https://www.npmjs.com/package/json-server)

Para instalar o projeto **json-server** rode o seguinte comando:

```bash
$ npm install -g json-server
```

Você deve criar um json para servir como base para sua API.

```bash
$ touch db.json
```

Inserir o seguinte código dentro do seu `db.json`:

```json
{
  "meu_objeto": [
    {
      "id": 1,
      "nome": "Paulo",
      "sobrenome": "Pinheiro"
    },
    {
      "id": 2,
      "nome": "Joana",
      "sobrenome": "Silva"
    }
  ]
}
```


Para rodar o json-server executar o sequinte comando:

```bash
$ json-server --watch db.json
```

## Para executar o projeto, basta instalar as dependencias e rodar o server

```bash
$ pip install -r requirements.txt
$ python manage.py runserver
```

