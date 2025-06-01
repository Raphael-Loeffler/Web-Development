from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def items():
    return render_template('items/items.html')

if __name__ == "__main__":
    app.run(debug=True)