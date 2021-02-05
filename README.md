# star-war-planets-api

# Desafio B2W
## Inicialização do Projeto

```bash
$ docker-compose up --build
```
## Execução de teste

```bash
$ python3 -u -m pytest test/
```
## Endpoints

|           Url           | Method |    Action     |
| :---------------------: | :----: | :-----------: |
|      /api/planets       |  GET   | List Planets  |
|    /api/planets/:id     |  GET   | Return Planet |
| /api/planets/name/:name |  GET   | Return Planet |
|      /api/planets       |  POST  | Store Planet  |
|    /api/planets/:id     | DELETE | Remove Planet |


# Listar Planetas - GET - localhost:8080/api/planets

## Response
```json
[
    {
        "_id": {
            "$oid":"5c7da13a53af6f26842e1974"
        },
        "name": "Alderaan",
        "climate": "temperate",
        "terrain": "jungle",
        "movie_appearances_counter": 5
    }
]

```
# Recuperar planet pelo id - GET - localhost:8080/api/planets/<:id>

## Response
```json

{
    "_id": {
        "$oid":"5c7da13a53af6f26842e1974"
    },
    "name": "Alderaan",
    "climate": "temperate",
    "terrain": "jungle",
    "movie_appearances_counter": 5
}

```

# Recuperar planet pelo nome - GET - localhost:8080/api/planets/name/<:name>

## Response
```json

{
    "_id": {
        "$oid":"5c7da13a53af6f26842e1974"
    },
    "name": "Alderaan",
    "climate": "temperate",
    "terrain": "jungle",
    "movie_appearances_counter": 5
}
```
# Criar planeta - POST - localhost:8080/api/planets

## Request Body
```json
{
    "name": "Alderann",
    "climate": "temperate",
    "terrain": "jungle"
}

```
## Response
```json
{
    "_id": "601d6669ca2e985a264775fa"
}

```