from flask import Flask, render_template, request, redirect
from game import Game

app = Flask(__name__)
game = Game()

from collections import defaultdict

@app.route("/")
def index():
    cards_by_type = defaultdict(list)
    for card in game.cards:
        cards_by_type[card.type].append(card)

    return render_template(
        "index.html",
        cards_by_type=cards_by_type,
    )


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
