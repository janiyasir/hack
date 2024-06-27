from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Update the database URI with your own credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host/database_name'
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
            username = request.form.get('username')
            password = request.form.get('password')
            
            # Retrieve the user from the database
            user = User.query.filter_by(username=username).first()
            
            if user and user.password == password:
                # Password is correct, redirect to a logged-in page
                return redirect('https://www.facebook.com')
            else:
                # Username or password is incorrect, handle appropriately
                return "Incorrect username or password"
        
        return "Method not allowed", 405  # Handle other HTTP methods if necessary

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
