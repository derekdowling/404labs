from flask import Flask, request, redirect, g, url_for, abort, render_template, flash, session
import sqlite3

# configuration
DATABASE = '/tmp/taskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'user'
PASSWORD = 'pw123'

app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE'])


@app.teardown_request
def teardown(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def insert_task(task):
    g.db.execute('insert into tasks(category, priority, description) values(?, ?, ?)',
          [task["category"], task["priority"], task["description"]],
          one=True
    )
    g.db.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('tasks'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('tasks'))


@app.route('/task', methods=['POST'])
def add_task():
    # POST adds another task to the list
    if request.method == 'POST':
        if not session.get('logged_in'):
            abort(401)

        # if logged in, add new task
        category = request.form['category']
        priority = request.form['priority']
        description = request.form['description']
        insert_task({
            "category": category,
            "priority": priority,
            "description": description
        })

        flash('New task was successfully added')
        print("here")
        return redirect(url_for('tasks'))

@app.route('/', methods=['GET'])
def tasks():
    cur = g.db.execute('select category, priority, description from tasks order by id desc')
    tasks = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    temp = render_template('tasks.html', tasks=tasks)
    print(temp)
    return temp

if __name__ == '__main__':
    app.run(debug=True)
