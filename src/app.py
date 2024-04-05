from flask import Flask
from src.services.routes import service_bp
from src.helloWorld.routes import helloWorld_bp
from src.sell.routes import sell_bp
from flasgger import Swagger

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # Toutes les règles correspondent
            "model_filter": lambda tag: True,  # Tous les modèles
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, config=swagger_config)

app.register_blueprint(helloWorld_bp, url_prefix='/service')
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(sell_bp, url_prefix='/service/sell')

if __name__ == "__main__":
    app.run(debug=True, port=500)
