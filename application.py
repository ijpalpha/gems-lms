from flask import Flask, render_template

application = Flask(__name__)

app = application

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/course-page')
def course_page():
    return render_template('course_page.html')

if __name__ == '__main__':
    app.run(debug=True)