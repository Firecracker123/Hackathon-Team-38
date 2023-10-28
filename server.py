from flask import Flask, render_template
from game import Game
app = Flask(__name__)

game = Game()

@app.route("/")
def main():
    return render_template("mainpage.html", description=game.description, image_url="/static/images/test_scene.jpeg")

@app.route("/game")
def start():
    pass

@app.route("/update", methods=["POST"])
def update():
    pass


if __name__ == "__main__":
    app.run(debug=True)