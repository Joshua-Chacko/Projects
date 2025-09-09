from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# connect to SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    habit = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def HomePage():
    # grabs all the values in the database
    entries = Habit.query.all()
    return render_template('home.html', active_page='home', entries=entries)
    
@app.route('/habits', methods=['POST'])
def habits():
    new_habit = Habit(habit=request.form['user_input'])
    db.session.add(new_habit)
    db.session.commit()
    return redirect('/')

@app.route('/analytics') 
def analytics():
    return render_template('analytics.html', active_page='analytics')
if __name__ == '__main__':
    app.run(debug=True)