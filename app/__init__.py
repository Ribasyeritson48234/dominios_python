from flask import Flask

## crar el objeto principal 
app = Flask(__name__)

#importal a las rutas definidas 
from app import routes

if __name__ == "__main__":
    app.run()