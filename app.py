from flask import Flask, render_template, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# About us page
@app.route('/about-us')
def about():
    return render_template('about.html')

# Sign up / Login page
@app.route('/sign-in')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    app.run()