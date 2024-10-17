from flask import Flask, render_template, request, redirect, flash
import sqlite3
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Database initialization
def init_db():
    conn = sqlite3.connect('form_submissions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        ip_address = request.remote_addr
        today = datetime.date.today()

        # Check if the user has already submitted today
        conn = sqlite3.connect('form_submissions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM submissions WHERE ip_address=? AND date=?", (ip_address, today))
        existing_submission = cursor.fetchone()

        if existing_submission:
            flash("You have already submitted your attendance today.")
        else:
            cursor.execute("INSERT INTO submissions (name, course, ip_address, date) VALUES (?, ?, ?, ?)",
                           (name, course, ip_address, today))
            conn.commit()
            flash("Attendance submitted successfully!")

        conn.close()

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
