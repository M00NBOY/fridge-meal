# -*- coding:utf-8 -*-

from database import db
from flask import Flask, request, jsonify

import os.path

from models import Product, Recipe

app = Flask(__name__)

error_msg = [
    {"name": "Glissez-déposez un ingrédient pour trouver une recette adaptée !"}
]
await_product = [
    {"name": "Glissez-déposez un ingrédient ici !!"}
]
products = []
recipes = []

def match(recipe, products):
    if products[0] == 'undefined':
        return jsonify(error_msg)
    else:
        for p in products:
            if int(p) not in recipe['products']:
                return False

    return True

# /recipes?products=34,28,90
@app.route('/recipes')
def search_recipes():
    products = request.args.get('products', "")

    if len(products) == 0 or products == 'undefined':
        return jsonify(error_msg)

    products = products.split(',')
    results = []

    for r in Recipe.query.all():
        recipes.append({'id': r.id, 'name': r.name})

    for r in recipes:
        if match(r, products):
            results.append(r)

    return jsonify(results)

@app.route('/products')
def search_products():
    for p in Product.query.all():
        products.append({'id': p.id, 'name': p.name})
        return jsonify(products)

@app.route('/add', methods=['POST'])
def add_recipes():
    # if request.get_json(force=True) or not 'name' in request.get_json(force=True:
        # abort(400)

    recipe = Recipe()
    recipe.name = request.get_json(force=True).name

    db.session.add(recipe)
    db.session.commit()

    return jsonify(recipe)

if __name__=='__main__':
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    dbpath = os.path.abspath(os.getcwd()) + '/db/matcher.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbpath

    db.init_app(app)

    with app.app_context():
        db.create_all()
        product = Product()
        recipe = Recipe()

        recipe.name = 'hareng pomme à l\'huile'
        product.name = 'hareng'

        recipe.products = [1]

        db.session.add(recipe)
        db.session.add(product)
        db.session.commit()

    app.run()
