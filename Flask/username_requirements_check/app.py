from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    username: str = request.args.get('username')
    
    requirements_failed = []
    
    if not contains_one_lowercase(username):
        requirements_failed.append(0)
    
    if not contains_one_uppercase(username):
        requirements_failed.append(1)
    
    if not contains_number_at_the_end(username):
        requirements_failed.append(2)
    
    return render_template('result.html', username=username, requirements_failed=requirements_failed)

def contains_one_lowercase(s):
    return any(char.islower() for char in s)

def contains_one_uppercase(s):
    return any(char.isupper() for char in s)

def contains_number_at_the_end(s):
    try:
        return ['0','1','2','3','4','5','6','7','8','9'].__contains__(s[-1])
    except:
        return False
    

if __name__ == '__main__':
    app.run(debug=True)