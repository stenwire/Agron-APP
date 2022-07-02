from itertools import product
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# from flask_moment import Moment
from sqlalchemy.sql import func

app = Flask(__name__)
# moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    contact = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)
    details = db.Column(db.Text)
    image_link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Farmer {self.firstname}>'


class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    contact = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)
    details = db.Column(db.Text)
    image_link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Investor {self.firstname}>'


class Trader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    contact = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)
    details = db.Column(db.Text)
    image_link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Trader {self.firstname}>'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    contact = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)
    details = db.Column(db.Text)
    image_link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Trader {self.firstname}>'


# ... home route

@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------------------
#   FARMERS
# --------------------------------------------

@app.route('/farmer')
def farmer():
    farmers = Farmer.query.all()
    return render_template('index.html', farmers=farmers)


# ...

@app.route('/farmer/<int:farmer_id>/')
def get_farmer(farmer_id):
    farmer = Farmer.query.get_or_404(farmer_id)
    return render_template('farmer.html', farmer=farmer)


# ...


@app.route('/farmer/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        details = request.form['details']
        image_link = request.form['image_link']
        farmer = Farmer(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio,
                          details=details,
                          image_link=image_link)
        db.session.add(farmer)
        db.session.commit()

        return redirect(url_for('farmer'))

    return render_template('create_farmer.html')


# ...


@app.route('/farmer/<int:farmer_id>/edit/', methods=('GET', 'POST'))
def edit(farmer_id):
    farmer = Farmer.query.get_or_404(farmer_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        farmer.firstname = firstname
        farmer.lastname = lastname
        farmer.email = email
        farmer.age = age
        farmer.bio = bio

        db.session.add(farmer)
        db.session.commit()

        return redirect(url_for('farmer'))

    return render_template('edit_farmer.html', farmer=farmer)


# ...

@app.post('/farmer/<int:farmer_id>/delete/')
def delete(farmer_id):
    farmer = Farmer.query.get_or_404(farmer_id)
    db.session.delete(farmer)
    db.session.commit()
    return redirect(url_for('farmer'))


# -------------------------------------------
#   INVESTOR
# --------------------------------------------

@app.route('/investor/<int:investor_id>/')
def investor(investor_id):
    investor = Investor.query.filter_by(investor_id)
    product = Product.query.filter(Product.id == investor.id)
    return render_template('investor.html', product=product)

@app.post('/investor/explore')
def get_stock():
    product = Product.query.get_or_404()

    return render_template('stock.html', products=product)


@app.route('/farmer/create/', methods=('GET', 'POST'))
def create_investor():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        details = request.form['details']
        image_link = request.form['image_link']
        farmer = Farmer(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio,
                          details=details,
                          image_link=image_link)
        db.session.add(farmer)
        db.session.commit()

        return redirect(url_for('investor'))

    return render_template('create_investor.html')

@app.route('/investor/<int:investor_id>/edit/', methods=('GET', 'POST'))
def edit_investor(investor_id):
    investor = Investor.query.get_or_404(investor_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        investor.firstname = firstname
        investor.lastname = lastname
        investor.email = email
        investor.age = age
        investor.bio = bio

        db.session.add(farmer)
        db.session.commit()

        return redirect(url_for('investor'))

    return render_template('edit_investor.html', farmer=farmer)


@app.post('/investor/<int:investor_id>/delete/')
def delete_investor(investor_id):
    investor = Farmer.query.get_or_404(investor_id)
    db.session.delete(investor)
    db.session.commit()
    return redirect(url_for('farmer'))


# -------------------------------------------
#   TRADER
# --------------------------------------------

@app.route('/farmer/<int:trader_id>/')
def trader(trader_id):
    traders = Trader.query.get_or_404(trader_id)
    return render_template('farmer.html', traders=traders)


@app.route('/trader/create/', methods=('GET', 'POST'))
def create_trader():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        details = request.form['details']
        image_link = request.form['image_link']
        trader = Trader(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio,
                          details=details,
                          image_link=image_link)
        db.session.add(trader)
        db.session.commit()

        return redirect(url_for('trader'))

    return render_template('create_trader.html')


@app.route('/trader/<int:trader_id>/edit/', methods=('GET', 'POST'))
def edit_trader(investor_id):
    trader = Trader.query.get_or_404(investor_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        trader.firstname = firstname
        trader.lastname = lastname
        trader.email = email
        trader.age = age
        trader.bio = bio

        db.session.add(farmer)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_trader.html', farmer=farmer)


@app.post('/trader/<int:trader_id>/delete/')
def delete_trader(investor_id):
    trader = Farmer.query.get_or_404(investor_id)
    db.session.delete(trader)
    db.session.commit()
    return redirect(url_for('index'))


# -------------------------------------------
# PRODUCTS/ SHOP
# ---------------------------------------------

@app.route('/shop')
def shop():
    product = Product.query.all()
    return render_template('shop.html', products=product)


@app.route('/product/<int:product_id>/')
def get_product(product_id):
    product_id = Product.query.get_or_404(product_id)
    return render_template('farmer.html', products=product)

@app.route('/product/create/', methods=('GET', 'POST'))
def add_product():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        details = request.form['details']
        image_link = request.form['image_link']
        product = Product(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio,
                          details=details,
                          image_link=image_link)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('shop'))

    return render_template('create_product.html')