from flask import Flask, render_template, request, session, redirect
from db.models import getAllProducts, getRangeProducts, getUser

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

@app.route("/admin")
def adminPage():
    # Перенаправление пользователя, если он не зарегестрирован
    if "login" not in session:
        return redirect("/admin/login")

@app.route("/admin/login", methods=["GET", "POST"])
def adminLoginPage():
    if request.method == "GET":
        return render_template("adminLogin.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]




app.run(debug=True)
