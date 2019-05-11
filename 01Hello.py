from flask import Flask


app = Flask(__name__)


@app.route("/hello/<name>")
def hello_word(name):
    return "hello %s!" % name

if __name__ == '__main__':
    app.run(debug=True)