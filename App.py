from flask import Flask
from routes.routes import routes_bp
app = Flask(__name__)

app.register_blueprint(routes_bp, url_prefix = '/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8081)