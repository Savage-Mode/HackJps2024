from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static') 

htmlcode = "<p>hello people, its a me, ashwin</p>"

@app.route("/")
def hello_world():
    return htmlcode
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)