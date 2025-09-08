from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def HomePage():
    # Pass active_page parameter to template for navigation highlighting
    return render_template('home.html', active_page='home')

@app.route('/habits')
def habits():
    return render_template('habits.html', active_page='habits')

@app.route('/analytics') 
def analytics():
    return render_template('analytics.html', active_page='analytics')
if __name__ == '__main__':
    app.run(debug=True)