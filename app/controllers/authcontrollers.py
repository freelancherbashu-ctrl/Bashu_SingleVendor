from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models.user_model import User

class AuthController:
    
    def login(self):
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            
            user = User.find_by_email(email)
            
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['user_name'] = user['name']
                flash('Login successful!', 'success')
                return redirect(url_for('authroutes.home'))
            else:
                flash('Invalid email or password', 'error')
                return redirect(url_for('authroutes.login'))
        
        return render_template('login.html')
    
    def register(self):
        # Register logic (पहिले बनाइसक्नुभयो)
        pass
    
    def home(self):
        if 'user_id' not in session:
            return redirect(url_for('authroutes.login'))
        return render_template('home.html', name=session.get('user_name'))
    
    def logout(self):
        session.clear()
        flash('Logged out successfully', 'success')
        return redirect(url_for('authroutes.login'))