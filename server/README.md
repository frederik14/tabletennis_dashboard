# Player

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all players

**Definition**

`GET /players`

**Response**

- `200 OK` on success

```json
[
    {
        "id": 2,
        "name": "Flore",
        "rank": 1
    },
    {
        "id": 1,
        "name": "Frederik",
        "rank": 2
    }
]
```

### Registering a new player

**Definition**

`POST /players`

**Arguments**

```json
    {
        "name": "Flore",
    }
```

If a device with the given name already exists error 400 will be given.

**Response**

- `201 Created` on success

```json
{
    "message": "Created new player.",
    "player": {
        "id": 4,
        "name": "test2",    
        "rank": 4
    }
}
```
### List all games

**Definition**

`GET /games`

**Response**

- `200 OK` on success

```json
[
    {
        "home_player": "Frederik",
        "home_sets": 0,
        "id": 3,
        "out_player": "Flore",
        "out_sets": 0
    },
    {
        "home_player": "Frederik",
        "home_sets": 0,
        "id": 4,
        "out_player": "Flore",
        "out_sets": 2
    }
]
```

### Registering a new game

**Definition**

`POST /games`

**Arguments**

```json
    {
        "home_player": "Frederik",
        "out_player": "Flore"
    }
```

If a player didn't exist it will give error 400.

**Response**

- `201 Created` on success

```json
    {
        "game": {
            "home_player": "Frederik",
            "home_sets": 0,
            "id": 5,
            "out_player": "Flore",
            "out_sets": 0
        },
        "message": "Created new player."
    }
```

### Set result for an existing game

**Definition**

`PUT /games`

**Arguments**

The id is received when creating a game of by getting all games.

```json
    {
        "id" : 4,
        "home_sets" : 1,
        "out_sets" : 2
    }
```

If the game doesn't exist you will get error 400.
If the game is a draw it is set to 0-0. (draws are not excepted)

**Response**

- `201 Created` on success

```json
    {
    "message": "Game result is set.",
    "player": {
        "home_player": "Frederik",
        "home_sets": 1,
        "id": 6,
        "out_player": "Flore",
        "out_sets": 2
        }
    }
```

## Delete a device

**Definition**

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success
