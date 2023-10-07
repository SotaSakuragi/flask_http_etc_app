from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# hello関数のレンダーテンプレートで変数nameを使う
@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
