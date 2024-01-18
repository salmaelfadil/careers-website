from flask import Flask, render_template

app = Flask(__name__)

SPOTS = [{
    'id': 1,
    'location': 'mall'
}, {
    'id': 2,
    'location': 'street'
}, {
    'id': 1,
    'location': 'mall'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", spots=SPOTS, city="Barcelona")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
