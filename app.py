# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "bot_database.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the bot_info table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bot_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def get_paginated_bot_info(page):
    ROWS_PER_PAGE = 10
    offset = (page - 1) * ROWS_PER_PAGE

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Retrieve paginated bot information from the database
    cursor.execute("SELECT * FROM bot_info ORDER BY id DESC LIMIT ? OFFSET ?", (ROWS_PER_PAGE, offset))
    paginated_bot_data = cursor.fetchall()

    conn.close()

    return paginated_bot_data

@app.route('/')
def index():
    return "Welcome to the Bot Website!"

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    # Handle admin login logic here
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    page = int(request.args.get('page', 1))
    paginated_bot_data = get_paginated_bot_info(page)
    return render_template('admin_dashboard.html', bot_data=paginated_bot_data)

# Define routes for adding, editing, and deleting bot information here

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
