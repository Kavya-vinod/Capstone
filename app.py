from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

# Dummy user data for demonstration
users = {}
# Dummy list to store items
items = []

@app.route('/')
def home():
    return """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-image: url('https://source.unsplash.com/1600x900/?nature');
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 20px;
            color: #ffffff;
        }
        
        .container {
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }
        
        h1 {
            color: #ffffff;
            font-weight: bold;
            font-size: 48px;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        p {
            margin: 10px 0;
            color: #ffffff;
        }
        
        a {
            color: #ffffff;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        a:hover {
            color: #cccccc;
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            text-decoration: none;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
    <div class="container">
        <h1>Welcome to the Home Page!</h1>
        <p><a href='/login' class="btn">Login</a></p>
        <p><a href='/register' class="btn">Register</a></p>
    </div>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('main'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('register'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash("Username already exists")
        else:
            users[username] = password
            flash("Registration successful")
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Add item to the list
        item = request.form.get('item')
        if item:
            items.append(item)
    return render_template('main.html')

@app.route('/display')
def display():
    return render_template('display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
