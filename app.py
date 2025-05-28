from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    if not os.path.exists('data.db'):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            interests TEXT,
            likes TEXT,
            dislikes TEXT,
            habits TEXT
        )''')
        conn.commit()
        conn.close()

# Home route with form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].strip()
        age = request.form['age']
        interests = ','.join([request.form[f'interest{i}'].strip() for i in range(1, 6)])
        likes = ','.join([request.form[f'like{i}'].strip() for i in range(1, 6)])
        dislikes = ','.join([request.form[f'dislike{i}'].strip() for i in range(1, 6)])
        habits = ','.join([request.form[f'habit{i}'].strip() for i in range(1, 6)])

        # Basic validation
        if not name or not age.isdigit() or int(age) < 0 or int(age) > 150:
            return render_template('index.html', error="Invalid name or age")

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''INSERT INTO responses (name, age, interests, likes, dislikes, habits)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (name, int(age), interests, likes, dislikes, habits))
        conn.commit()
        conn.close()
        return redirect(url_for('thank_you'))

    return render_template('index.html', error=None)

# Thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
