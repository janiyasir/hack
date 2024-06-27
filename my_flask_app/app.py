from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            if username and password:
                # Simulate authentication (replace with your actual logic)
                if username == 'demo' and password == 'password':
                    # Redirect to a success page or do further processing
                    return redirect('https://www.example.com/success')
                else:
                    return "Incorrect username or password"
            else:
                return "Username or password cannot be empty"

        return "Method not allowed", 405  # Handle other HTTP methods if necessary

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
