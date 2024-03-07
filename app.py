from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('main.html')


@app.route('/items')
def market():
    return render_template('items.html')


@app.route('/cart')
def news():
    return render_template('cart.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
