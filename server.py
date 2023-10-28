from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("mainpage.html", image_url="")

@app.route("/game")
def start():
    pass

@app.route("/update", methods=["POST"])
def update():
    pass

@app.route("/imageurl")
def image_url():
    return "/static/test_scene.jpeg"

if __name__ == "__main__":
    app.run(debug=True)