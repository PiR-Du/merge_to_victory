from flask import Flask, render_template, request, redirect
from game import Game

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template("index.html", cards=game.cards)

@app.route("/combine", methods=["POST"])
def combine():
    id1 = int(request.form["card1"])
    id2 = int(request.form["card2"])
    game.combine(id1, id2)
    return redirect("/")

@app.route("/tick", methods=["POST"])
def tick():
    game.tick()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
