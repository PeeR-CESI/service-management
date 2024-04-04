from flask import Flask
from services.routes import service_bp
from avis.routes import avis_bp
from helloWorld.routes import helloWorld_bp

app = Flask(__name__)
app.register_blueprint(helloWorld_bp)
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(avis_bp, url_prefix='/avis')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
