from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')
    password = request.args.get('password')
    return render_template('thank_you.html', name=name, password=password)

if __name__ == "__main__":
    app.run()