
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Perform authentication
    if username == 'admin' and password == 'password123':
        return "Login successful!"
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    app.run()