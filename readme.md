# Calculate distance from two addresses

This application uses Positionstack API to get coordinates and calculates the distance from one specific point of origin to the provided address creating a csv log file with the results. In this example, the application calculates the distance from Saint Basil's Cathedral and the address provided in the client. Saint Basil's Cathedral is used as an approximation to define whether the provided address is located inside the MKAD Moscow Ring Road (MKAD) or not. It's location is the center point of a 18 km radius circle. Will return a null string, indicating the address is inside MKAD, or a string with the distance expressed in kilometers if the address falls outside the MKAD.

You will need to sign up for a free and straight forward API Key at [positionstack](https://positionstack.com/product)

### How to run the application

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `flask run`

### Para rodar os testes de integração

- `pytest`

# Endpoints

## User

Este endpoint possui duas rotas: uma rota para cadastro de usuários e uma rota para o login de usuários.

### Point Request

Rota para **cadastro** de um novo usuário.

```markdown
POST https://criptofacil-deploy.herokuapp.com/api/register
```

### JSON Content

```json
{
  "name": "<nome>",
  "last_name": "<sobrenome>",
  "email": "<nome@mail.com>",
  "password": "<senha>"
}
```

### Response Format

```json
{
	"id": "<id>"
	"name": "<nome>",
	"last_name": "<sobrenome>",
	"email": "<nome@mail.com>"
}
```
