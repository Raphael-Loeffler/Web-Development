#TASK 1: Import whatever is necessary
from flask import Flask, request, render_template

#TASK 2: Create a Flask app
app = Flask(__name__)

# TASK 3:Create the decorator for the index function
@app.route('/')
def index():
    # Welcome Page
    # Create a generic welcome page.
    return render_template('index.html')
# TASK 4: Create the decorator for the greeting function
@app.route('/<name>')
def greeting(name):
    # This function will take in the name passed
    # and then use "greeting" to convert it to a 
    # readable string as a greeting!
    return f"Greetings, {name}"

if __name__ == '__main__':
    #TASK 5: Run the app
    app.run()