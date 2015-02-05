from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)
dbFile = 'db1.db'
conn = None


def connect():
    global conn
    if conn is None:
        conn = sqlite3.connect(dbFile)
        conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def disconnect():
    global conn
    if conn is None:
        conn.close()
        conn = None


def query(query, args=(), one=False):
    cur = connect().cursor()
    cur.execute(query, args)
    r = cur.fetchall()
    cur.close()
    return (r[0] if r else None) if one else r


def add_task(task):
    query('insert into tasks(category, priority, description) values(?, ?, ?)',
          [task["category"], task["priority"], task["description"]],
          one=True
    )
    connect().commit()


def format_tasks():
    tasks = query('select * from tasks')

    for task in tasks:
        print("Task(category): %s " % task['category'])

    print("%d tasks in total." % len(tasks))


@app.route('/')
def home():
    return '<h1>All The Tasks!<h1>'


@app.route('/task', methods=['GET', 'POST'])
def task():
    # POST
    if request.method == 'POST':
        category = request.form['category']
        priority = request.form['priority']
        description = request.form['description']
        add_task({
            "category": category,
            "priority": priority,
            "description": description
        })

        # return redirect('/task1')
        return redirect(url_for('task'))

    # GET
    resp = ''
    resp = resp + '''
    <form action="" method="POST">
        <p>Category<input type=text name="category"></p>
        <p>Priority<input type=number name="priority"</p>
        <p>Description<input type=text name="description"</p>
        <p><input type=submit value=Add></p>
    </form>
    '''
    # Show table
    resp = resp + '''
    <table border = "1" cellpading="4">
        <tbody>
            <tr>
                <th>Category</th>
                <th>Priority</th>
                <th>Description</th>
            </tr>
    '''

    for task in query('select * from tasks'):
        resp += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (task['category'], task['priority'], task['description'])

    resp += '</tbody></table>'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
