# MyRealToDo

Pequeno projeto para uso pessoal e estudo de diversos topicos, sendo alguns deles os seguintes:
- Python
- Flask
- API REST
- DB (SQLite e PostgreSQL)
- Frontend
- Git
- Testes unitarios
- CI/CD
- Infraestrutura para a aplicacao
- Monitoramento

Basicamente entender e reproduzir todo o ciclo de vida da aplicacao, e me divertir um pouco durante o processo :smile: .

## TODOs 

- Adicionar suporte ao PostgreSQL
- Corrigir o tratamento de conexoes no banco (sem ORM)
- Desenvolver frontend para consumir a API REST

## Endpoints

| Método  | Endpoint             | Ação                             |
|---------|----------------------|----------------------------------|
| GET     | /api/v1.0/tasks      | Lista todas as tarefas           |
| GET     | /api/v1.0/tasks/<id> | Obtém mais informações da tarefa |
| POST    | /api/v1.0/tasks      | Cria uma nova tarefa             |
| PUT     | /api/v1.0/tasks/<id> | Atualiza uma tarefa              |
| DELETE  | /api/v1.0/tasks/<id> | Deleta uma tarefa                |


## Modelo de dados

| Campo      | Tipo de dado | Constraint                |
|------------|--------------|---------------------------|
| id         | INTEGER      | PRIMARY KEY AUTOINCREMENT |
| nome      | TEXT         | NOT NULL                  |
| prioridade | TEXT         | NOT NULL                  |
| status     | TEXT         | NOT NULL                  |
| depende    | TEXT         | -                         |

## Referencias

[Designing a RESTful API with Python and Flask - miguelgrinberg.com](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
