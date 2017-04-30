# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)


products= [
    {"id": 1, "name": "pomme"},
    {"id": 2, "name": "steak"},
    {"id": 3, "name": "fromage"}
]

recipes = [
    {"id": 1, "name": "tarte", "products":[2, 1]},
    {"id": 2, "name": "blanquette", "products": [3]},
    {"id": 3, "name": "pareo", "products": [2, 3]}
]

def match(recipe, products):
    for p in products:
        if int(p) not in recipe['products']:
            print(int(p))
            return False

    return True

# /recipes?products=34,28,90
@app.route('/recipes')
def search_recipes():
    products = request.args.get('products', "")

    if len(products) == 0:
        return jsonify(recipes)


    products = products.split(',')
    results = []

    for r in recipes:
        if match(r, products):
            results.append(r)

    return jsonify(results)

@app.route('/products')
def search_products():
    return jsonify(products)

if __name__=='__main__':
	app.run(debug=True)
