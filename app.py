from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
import random
import string

app = Flask(__name__)
app.secret_key = "".join(random.choices(string.ascii_letters, k=256))

@app.route("/")
def top_page():
    return render_template("index.html")

@app.route("/add")
def add():
    # formからデータの取得
    id = request.args.get("id")
    name = request.args.get("name")

    # sessionの有効期限の設定
    session.permanent = True    # セッションの有効期限設定(デフォルト3日)
    app.permanent_session_lifetime = timedelta(minutes=30)  # 有効期限の値の設定

    if not "cart" in session:
        product_list = []
        product_list.append([id,name])
        session["cart"] = product_list
    else :
        product_list = session.pop("cart", None)
        product_list.append([id,name])
        session["cart"] = product_list

    print(session["cart"])

    return render_template("index.html")

@app.route("/cart_list")
def cart_list():
    if "cart" in session:
        return render_template("list.html", list=session["cart"])
    else:
        return render_template("not_list.html")

@app.route("/buy")
def buy():
    if "cart" in session:
        product_list = session.pop("cart", None) # カートの中身削除

        # 実際の購入処理は省略
        print(product_list)

        return render_template("result.html")
    else:
        return redirect(url_for("error_page"))

@app.route("/error")
def error_page():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)