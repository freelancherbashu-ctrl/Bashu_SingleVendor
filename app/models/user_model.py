from app.models.database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    
    @staticmethod
    def create(name, email, password):
        db = get_db()
        cursor = db.cursor()
        hashed_password = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )
        db.commit()
        user_id = cursor.lastrowid
        db.close()
        return user_id
    
    @staticmethod
    def find_by_email(email):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        db.close()
        return user