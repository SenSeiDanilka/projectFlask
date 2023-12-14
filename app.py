from flask import Flask, render_template, request, session, redirect
from db.models import getAllProducts, getRangeProducts, getUser

app = Flask(__name__)
app.secret_key = "secret key"

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
    
    return render_template("admin.html", login=session["login"])

@app.route("/admin/login", methods=["GET", "POST"])
def adminLoginPage():
    if request.method == "GET":
        return render_template("adminLogin.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        user = getUser(login, password)

        if user:
            session["login"] = user[1]
            return redirect("/admin")
        else:
            return render_template("adminLogin.html", error="Логин или пароль введены неправильно")


app.run(debug=True)
