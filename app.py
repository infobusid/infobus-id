from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data user (dalam contoh ini, kita menggunakan data dummy)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
        else:
            return 'Username atau password salah'
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return 'Selamat datang di dashboard!'

if __name__ == '__main
