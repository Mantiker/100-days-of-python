import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("blog.html", posts=posts)

@app.route("/blog/<int:id>")
def post(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    for post in posts:
        if post["id"] == id:
            return render_template("post.html", post=post)

    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)