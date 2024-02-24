import random

from flask import Flask

app = Flask(__name__)

r_number = random.randint(0, 9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1><img width=200 src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/number/<int:number>")
def guess(number):
    if number > r_number:
        return "<h1>Too high. Try again!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < r_number:
        return "<h1>Too low. Try again!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1>You made it! The number is guessed</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)