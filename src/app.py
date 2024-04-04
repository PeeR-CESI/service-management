from flask import Flask
from services.routes import service_bp

app = Flask(__name__)
app.register_blueprint(service_bp, url_prefix='/service')

if __name__ == "__main__":
    app.run(debug=True, port=5001)