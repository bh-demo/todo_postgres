from flask import Flask , render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create flask app
app = Flask(__name__)
# initialise database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#define db model
class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # cannot be left blank
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        var1 = request.form['content'] # store form returns in var1
        newTask = todo(content=var1) # create new task. Pass var1 to content in db
        try:
            db.session.add(newTask) # cannot add var1, needs propoer formatted db
            db.session.commit()
            return redirect('/')
        except:
            return 'ERROR. could not add new Task'
        
    else:
        tasks = todo.query.order_by(todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    delTask = todo.query.get_or_404(id)

    try:
        db.session.delete(delTask)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content'] # content replaced in the db

        try:
            db.session.commit() # db only needs a commit
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
