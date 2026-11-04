Esto es simplemente una explicacion de cada paquete necesario para que todo funcione

# uvicorn: 
Es el servidor web local encargado de recibir y manejar las peticiones https para la aplicacion

# FastAPI:
Es un framework ligero y rapido que permite la creacion de API's (Aplication Programming Interfaces) para python (Compatible con pydantic)

# Pydantic
Es una biblioteca de validacion y modelado de datos, funciona como un filtro de seguridad y traductor automatico para los datos de la aplicacion para que todo siga el formato esperado

# Sqlalchemy
Funciona como un puente entre la aplicacion y la base de datos, con el objetivo de permitirme consultar, y trabajar con bases de datos utilizando codigo de python y no del mismo sql (increible con pydantic)
- **pip install sqlalchemy[asyncio]**
	Instalamos esta especificamente por el asyncio que le permite realizar tareas de forma asincrona (sin que el server se detenga a esperar la respuesta de lo que vayamos a hacer con la base de datos)

# Dotenv
Se encarga de las variables de entorno.

# psycopg
Es el adaptador para postgreSQL, como un puente o conector que permite a los scripts de Python comunicarse directamente con una base de datos PostgreSQL para ejecutar consultas SQL

# SQLModel
fusionar SQLAlchemy y Pydantic en una sola clase (al final no se uso)

 


