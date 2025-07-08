from flask import Flask, render_template, request
from models import create_all_tables
from models.user import get_user_by_credentials, create_user, get_user_by_username


app = Flask(__name__)
app.config['SECRET_KEY'] = 'w2w12121'

@app.before_request
def init_db():
    create_all_tables()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    status = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_credentials(username, password)

        if user:
            message = "Login successful!"
            status = "success"
        else:
            message = "Invalid username or password!"
            status = "error"

    return render_template('login.html', message=message, status=status)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
    status = ""

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        existing_user = get_user_by_username(username)

        if existing_user:
            message = "Username already exists!"
            status = "error"
        else:
            create_user(username, email, password)
            message = "Signup successful! Please login."
            status = "success"

    return render_template('signup.html', message=message, status=status)

if __name__ == '__main__':
    app.run(debug=True)
