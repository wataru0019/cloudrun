from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, this is a test deployment!"

@app.route("/data")
def data():
  data = {
    name: "Wataru",
    id: "15",
    age: "33",
    _from: "JP"
  }

if __name__ == "__main__":
  app.run(debug=True)