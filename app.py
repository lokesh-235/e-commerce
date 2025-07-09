from flask import Flask, render_template, request, redirect, url_for, session
from models import create_all_tables
from models.user import get_user_by_credentials, create_user, get_user_by_username


app = Flask(__name__)
app.config['SECRET_KEY'] = 'w2w12121'

@app.before_request
def init_db():
    create_all_tables()

from models.product import get_all_products

@app.route('/')
def home():
    products = get_all_products()
    print(products)
    return render_template('index.html', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    status = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_credentials(username, password)
        print(user)
        if user:
            session['user_id'] = user[0]         # user[0] = id
            session['username'] = user[1]        # user[1] = username
            return redirect(url_for('dashboard'))
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

from models.product import get_all_products
from models.order import get_orders_by_user

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    username = session['username']

    # Get all products (recommendations can replace this later)
    products = get_all_products()

    # Get order history for the user
    orders = get_orders_by_user(user_id)

    return render_template('dashboard.html', username=username, products=products, orders=orders)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
