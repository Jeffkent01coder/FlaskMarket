from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    # dictionaries to holds data using jinja
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'Playstation', 'barcode': '9456646732438', 'price': 47770}
    ]
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
