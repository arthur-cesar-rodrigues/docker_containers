from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def raiz():
    return "<p>Bem vindo a rota raiz!</p>"

@app.route("/site")
def site():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)