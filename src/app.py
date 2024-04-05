from flask import Flask
from flasgger import Swagger
from services.routes import service_bp
from avis.routes import avis_bp
from helloWorld.routes import helloWorld_bp

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

app.register_blueprint(helloWorld_bp)
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(avis_bp, url_prefix='/avis')

if __name__ == "__main__":
    app.run(debug=True, port=500)
