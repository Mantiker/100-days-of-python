import requests
from flask import Flask, redirect, render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()

posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    for post in posts:
        if post["id"] == id:
            return render_template("post.html", post=post)

    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)