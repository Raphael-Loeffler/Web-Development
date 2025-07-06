from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    username: str = request.args.get('username')
    
    has_lower_case: bool = any(char.islower() for char in username)
    has_upper_case: bool = any(char.isupper() for char in username)
    has_number_at_the_end: bool = f"{username[-1]}".isdigit()
    
    return render_template('result.html', username=username, has_lower_case=has_lower_case, has_upper_case=has_upper_case, has_number_at_the_end=has_number_at_the_end)

if __name__ == '__main__':
    app.run(debug=True)