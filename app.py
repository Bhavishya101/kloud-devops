
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, This is a simpleflask application <p>"

if __name__ == '__main__':
    app.run(debug=True)
