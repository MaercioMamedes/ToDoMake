# API ToDoMake


### Building

* [Após realizar o clone do projeto, crie um ambiente virtual python e instale as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* Caso não queira instanciar um banco de dados Postgresql, e queira rodar com o SQLite.
  * set a variável **DATABASE** no arquivo `setup/settings.py`:
  ``` 
  DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
  }
  ```
  
* Para usar a mesma configuração de banco de dados do projeto é necessário instanciar um banco postgres, e passar os parâmetros de conexão para variável `DATABASE` no arquivo `setup/settings.py`
  ### Endpoint

| URI    | METHOD | recurso    |
|--------|--------|------------|
| notes/ | POST   | criar nota |

### Payload

```
{
    "title": string,
    "content": string,
    "done": boolean
}
```

### Run

* Para executar a aplicação execute o seguinte comando:
`python manage.py runserver`
