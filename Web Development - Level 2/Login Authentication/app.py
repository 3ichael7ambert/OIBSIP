from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database (you should use a real database in production)
users = [
    {'username': 'user1', 'password': generate_password_hash('password1')},
    {'username': 'user2', 'password': generate_password_hash('password2')}
]

# Check if user is logged in
def is_logged_in():
    return 'username' in session

# Route for the secured page
@app.route('/secured')
def secured():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template('secured_page.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((user for user in users if user['username'] == username), None)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('secured'))
        else:
            return 'Login failed. Please check your credentials.'
    return render_template('login.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        if next((user for user in users if user['username'] == username), None):
            return 'Username already exists. Please choose another username.'
        
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Route for the homepage
@app.route('/')
def homepage():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
