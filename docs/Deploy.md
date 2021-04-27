# Deploy

## Environment structure

### Develop

* Create a file .env with the following key values configuration
```
MONGO_CONNECTION_STRING=mongodb://<user>:<password>@<ip>:<port>/pizzabot
DATABASE_NAME=pizzabot
COLLECTION_NAME=recommendations
APP_HOST=localhost
APP_PORT=5000
APP_DEBUG=true
```

* Run movies/main.py with python3

### Production

* Create a file .env with the following key values configuration
```
MONGO_CONNECTION_STRING=mongodb://user:password@<mongo_service_name>:<port>/pizzabot
DATABASE_NAME=pizzabot
COLLECTION_NAME=recommendations
APP_HOST=0.0.0.0
APP_PORT=5000
APP_DEBUG=False
```