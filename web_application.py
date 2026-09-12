from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(50), unique=True, nullable=False)
 password = db.Column(db.String(100), nullable=False)
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return f"User {username} logged in!"
        return "Invalid credentials"
    return render_template('login_register1.html')


with app.app_context():
 db.create_all()
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return 'User registered successfully!'
    return render_template('login_register1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
