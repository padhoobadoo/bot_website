# admin.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated admin credentials (insecure, just for demonstration purposes)
admin_credentials = {
    "username": "admin",
    "password": "admin123",
}

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == admin_credentials['username'] and password == admin_credentials['password']:
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    # Authenticate the admin session (you can use Flask-Login or similar for better security)
    return render_template('admin_dashboard.html', bot_data=bot_data)

if __name__ == '__main__':
    app.run(debug=True)
