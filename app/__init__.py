from flask import Flask
from app.routes.authroutes import AuthRoutes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'meropasal_secret_key_2025'
    
    # Register routes
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.get_routes())
    
    return app