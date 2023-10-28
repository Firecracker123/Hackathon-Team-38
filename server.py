from flask import Flask, render_template, request, redirect, url_for
import game
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("mainpage.html", image_url="")

@app.route("/game")
def start():
    pass

@app.route("/update", methods=["POST", "GET"])
def update():
    print("update()")
    jsdata = request.form['Submit']

    game.user_input(jsdata)

    return redirect(url_for('main'))

@app.route("/imageurl")
def image_url():
    room_name = game.world.data["current_state"]["room"]
    return game.world.data["rooms"][room_name]["img_url"]
    #return "static/images/main_menu.jpeg"
if __name__ == "__main__":
    app.run(debug=True)