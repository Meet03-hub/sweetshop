from flask import Flask, render_template, request, redirect, url_for
from sweetshop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '').lower()
    if search_query:
        sweets = shop.search_sweets(name=search_query, category=search_query)
    else:
        sweets = shop.view_sweets()
    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['POST'])
def add_sweet():
    sweet_id = int(request.form['id'])
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])

    shop.add_sweet(sweet_id, name, category, price, quantity)
    return redirect(url_for('index'))

@app.route('/delete/<int:sweet_id>', methods=['POST'])
def delete_sweet(sweet_id):
    shop.delete_sweet(sweet_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
