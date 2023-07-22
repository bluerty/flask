from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

# Flask-Reloaderを有効にする
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()