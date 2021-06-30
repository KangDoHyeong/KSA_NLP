from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>HelloWorld!</h1>"

@app.route("/hi")
def hi():
    return "<h1>HI!</h1>"

if __name__ == "__main__":
    app.run('172.31.7.178', debug=True, port = 9001)
