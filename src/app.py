from flask import Flask
from src.services.routes import service_bp
from src.helloWorld.routes import helloWorld_bp
from src.sell.routes import sell_bp

app = Flask(__name__)
app.register_blueprint(helloWorld_bp, url_prefix='/service')
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(sell_bp, url_prefix='/service/sell')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
