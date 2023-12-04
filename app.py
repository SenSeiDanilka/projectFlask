from flask import Flask, render_template, request
from db.models import getAllProducts, getRangeProducts

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/products", methods=["GET", "POST"])
def productsPage():
    if request.method == "GET":
        return render_template("products.html", products=getAllProducts())
    elif request.method == "POST":
        minPrice = request.form["min"]
        maxPrice = request.form["max"]
        return render_template("products.html", products=getRangeProducts(minPrice, maxPrice))

app.run(debug=True)
