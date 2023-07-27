# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "bot_database.db"
ROWS_PER_PAGE = 5  # Number of bot records per page

# ... (previous code)

def create_table():
    # ... (code to create the bot_info table)

def get_paginated_bot_info(page):
    # Calculate the offset based on the current page and rows per page
    ROWS_PER_PAGE = 10
    offset = (page - 1) * ROWS_PER_PAGE

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Retrieve paginated bot information from the database
    cursor.execute("SELECT * FROM bot_info ORDER BY id DESC LIMIT ? OFFSET ?", (ROWS_PER_PAGE, offset))
    paginated_bot_data = cursor.fetchall()

    conn.close()

    return paginated_bot_data


@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        bot_name = request.form['bot-name']
        bot_description = request.form['bot-description']

        # Insert the new bot information into the database
        insert_bot_info(bot_name, bot_description)

        return redirect(url_for('admin_dashboard'))

    # Pagination handling
    page = request.args.get('page', 1, type=int)
    paginated_bot_data = get_paginated_bot_info(page)

    return render_template('admin_dashboard.html', bot_data=paginated_bot_data, current_page=page)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
