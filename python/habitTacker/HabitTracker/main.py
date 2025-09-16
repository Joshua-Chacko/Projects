from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# connect to SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Habit(db.Model):
    __tablename__ = 'habits'
    habit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    habit = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Defines the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return f'<Habit {self.habit_name}>'
    

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    # Define the realtionship to the 'Habit' Model
    habits = db.relationship('Habit', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def HomePage():
    return render_template('home.html', active_page='home')
    
@app.route('/addhabits', methods=['POST'])
def add_habits():
    new_habit = Habit(habit=request.form['user_input'])
    db.session.add(new_habit)
    db.session.commit()
    return redirect('/')

@app.route('/habits')
def habits():
    entries = Habit.query.all()
    return render_template('habits.html', active_page='habits', entries=entries)

@app.route('/delete_habit', methods=['POST'])
def delete_habit():
    try:
        # Get the habit ID from the request
        habit_id = request.json.get('id')
        
        # Find the habit in the database
        habit = Habit.query.get(habit_id)
        
        if habit:
            # Delete the habit
            db.session.delete(habit)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Habit deleted successfully'})
        else:
            return jsonify({'success': False, 'message': 'Habit not found'}), 404
            
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/analytics') 
def analytics():
    return render_template('analytics.html', active_page='analytics')

if __name__ == '__main__':
    app.run(debug=True)