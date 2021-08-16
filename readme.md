# Calculate distance between two addresses

This application uses [positionstack](https://positionstack.com/) API to get coordinates and calculates the distance between two addresses creating a csv log file with the results. In this example, the application calculates the distance from Saint Basil's Cathedral and the address provided in the client. Saint Basil's Cathedral is used as an approximation to define whether the provided address is located inside the MKAD Moscow Ring Road (MKAD) or not. The Cathedral's location is the center point of a 18 km radius circle. It will return a null string if the distance is up to 18 km, indicating the address is inside MKAD, or a string with the distance, expressed in kilometers, indicating the address falls outside the MKAD.

You will need to sign up for a free and straight forward API key at [positionstack](https://positionstack.com/product).

### How to run the application

- `$ python -m venv venv`
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`
- `rename the .env.example file to .env`
- `insert your API Key in .env file`
- `$ flask run`

### How to run the application tests

- `$ pytest`

# Endpoints

## Distances

This enpoint will receive a json provided in the request body, verify the coordinates of the provided address using Positionstack API, calculate the distance from Saint Basil's Cathedral to the provided address and create a csv log file with the results following the application business logic.

### Point Request

```markdown
POST http://127.0.0.1:5000/api/distances/
```

### JSON Content

```json
{
  "address": "Khimki, Moscow Oblast, Russia, 141400"
}
```

### Response Format

```markdown
HTTP code: 201 CREATED
```

```json
{
  "id": "1",
  "address": "Khimki, MS, Russia",
  "distance": "19.57 km"
}
```

## Common API Errors:

| Code | Type                   | Description                               |
| ---- | ---------------------- | ----------------------------------------- |
| 400  | `BAD_REQUEST`          | Invalid key provided.                     |
| 422  | `UNPROCESSABLE_ENTITY` | Address must have at least 3 character's. |
| 422  | `UNPROCESSABLE_ENTITY` | Address must be a string.                 |
| 404  | `NOT_FOUND`            | Invalid or inexistent address.            |
