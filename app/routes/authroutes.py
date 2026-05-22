from flask import Blueprint
from app.controllers.authcontrollers import AuthController   # ✅ यसरी लेख्नुहोस्

class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint('authroutes', __name__)
        self.controller = AuthController()
    
    def get_routes(self):
        self.bp.route('/login', methods=['GET', 'POST'])(self.controller.login)
        self.bp.route('/register', methods=['GET', 'POST'])(self.controller.register)
        self.bp.route('/home')(self.controller.home)
        self.bp.route('/logout')(self.controller.logout)
        return self.bp